# Follow installation instructions from https://chainercv.readthedocs.io/en/stable/install.html

# Run in command line from the two respective folder locations with demo.py files in ChainerCV after downloading its repository

# ChainerCV Mask RCNN: https://github.com/chainer/chainercv/tree/master/examples/fpn
# Using the pretrained weight settings from a resnet that is 50 layers deep
python demo.py --model mask_rcnn_fpn_resnet50 <image>.jpg
# Using the pretrained weight settings from a resnet that is 101 layers deep
python demo.py --model mask_rcnn_fpn_resnet101 <image>.jpg

#ChainerCV Faster RCNN: https://github.com/chainer/chainercv/tree/master/examples/faster_rcnn
# Default weight settings is PASCAL VOC 2007
python demo.py <image>.jpg
# Using the pretrained weight settings from PASCAL VOC 2007 & 2012
python demo.py --pretrained-model "voc0712" <image>.jpg
