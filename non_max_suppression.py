import torch
from iou import intersection_over_union

def non_max_suppression(
    predictions,
    iou_threshold,
    prob_threshold,
    box_format="corners"
):
#predictions = [[class, class prob, x1,y1,x2,y2]]

    assert type(bboxes)==list

    bboxes=[box for box in bboxes if box[1]>prob_threshold]
    bboxes =sorted(bboxes,key=lambda x: x[1], reverse=True)
    bboxes_after_nms= []
    
    while bboxes:
        chosen_box=bboxes.pop(0)

        bboxes=[
            box
            for box in bboxes 
            if box[0]!= chosen_box[0]   # are they of diff classes
            or intersection_over_union(
                torch.tensor(chosen_box[2:]),
                box_format=box_format,
            )
            <iou_threshold
        ]
        bboxes_after_nms.append(chosen_box)
