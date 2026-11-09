#!/usr/bin/env python3
"""Pre-annotate 50 train images using Ultralytics pretrained model mapped to lab schema."""

from __future__ import annotations

import argparse
from pathlib import Path
from ultralytics import YOLO

# COCO class IDs to Lab Schema class IDs:
# Lab schema: 0: car, 1: truck, 2: bus, 3: van
# COCO classes: 2: car -> 0, 7: truck -> 1, 5: bus -> 2
COCO_TO_LAB = {
    2: 0,  # car -> car
    7: 1,  # truck -> truck
    5: 2,  # bus -> bus
}


def main():
    parser = argparse.ArgumentParser(description="Auto annotate train images with Ultralytics")
    parser.add_argument("--images", type=Path, default=Path("dataset/images/train"))
    parser.add_argument("--labels", type=Path, default=Path("dataset/labels/train"))
    parser.add_argument("--model", type=str, default="yolo11m.pt")
    parser.add_argument("--conf", type=float, default=0.25)
    parser.add_argument("--iou", type=float, default=0.50)
    args = parser.parse_args()

    args.labels.mkdir(parents=True, exist_ok=True)
    model = YOLO(args.model)

    image_paths = sorted(
        path for ext in ("*.jpg", "*.jpeg", "*.png")
        for path in args.images.glob(ext)
    )
    print(f"Loaded model {args.model}. Processing {len(image_paths)} images...")

    total_boxes = 0
    class_counts = {0: 0, 1: 0, 2: 0, 3: 0}

    for img_path in image_paths:
        results = model.predict(
            source=str(img_path),
            conf=args.conf,
            iou=args.iou,
            verbose=False,
            device="cpu"
        )
        result = results[0]
        boxes = result.boxes

        label_lines = []
        if boxes is not None and len(boxes) > 0:
            for box in boxes:
                coco_cls = int(box.cls[0].item())
                if coco_cls not in COCO_TO_LAB:
                    continue  # Ignore person, motorcycle, bicycle, etc.

                lab_cls = COCO_TO_LAB[coco_cls]
                # xywh normalized: [x_center, y_center, width, height]
                xywhn = box.xywhn[0].tolist()
                xc, yc, w, h = xywhn

                # Clamp to ensure strict [0, 1] bounds
                xc = max(0.0, min(1.0, xc))
                yc = max(0.0, min(1.0, yc))
                w = max(1e-4, min(1.0, w))
                h = max(1e-4, min(1.0, h))

                # Adjust if box edge exceeds 1
                if xc - w / 2 < 0:
                    w = 2 * xc
                if xc + w / 2 > 1:
                    w = 2 * (1 - xc)
                if yc - h / 2 < 0:
                    h = 2 * yc
                if yc + h / 2 > 1:
                    h = 2 * (1 - yc)

                label_lines.append(f"{lab_cls} {xc:.6f} {yc:.6f} {w:.6f} {h:.6f}")
                class_counts[lab_cls] += 1
                total_boxes += 1

        label_path = args.labels / f"{img_path.stem}.txt"
        label_path.write_text("\n".join(label_lines) + ("\n" if label_lines else ""), encoding="utf-8")

    print(f"Done! Generated {len(image_paths)} label files with {total_boxes} total boxes.")
    print(f"Class distribution: car (0): {class_counts[0]}, truck (1): {class_counts[1]}, bus (2): {class_counts[2]}, van (3): {class_counts[3]}")


if __name__ == "__main__":
    main()

