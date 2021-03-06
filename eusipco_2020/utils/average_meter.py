"""
This code is generated by Ridvan Salih KUZU @UNIROMA3
LAST EDITED:  03.04.2020
ABOUT SCRIPT:
It is a script for AvarageMeter .
"""


class AverageMeter(object):
    """Computes and stores the average and current value"""
    def __init__(self):
        self.reset()

    def reset(self):
        self.val = 0
        self.avg = 0
        self.sum = 0
        self.count = 0

    def update(self, val, n=1):
        self.val = val
        self.sum += val * n
        self.count += n
        self.avg = self.sum / self.count





