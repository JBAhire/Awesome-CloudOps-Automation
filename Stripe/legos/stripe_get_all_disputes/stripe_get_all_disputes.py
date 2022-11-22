##
##  Copyright (c) 2021 unSkript, Inc
##  All rights reserved.
##
import pprint
from pydantic import BaseModel
from typing import Dict


class InputSchema(BaseModel):
    pass


pp = pprint.PrettyPrinter(indent=2)


def legoPrinter(func):
    def Printer(*args, **kwargs):
        output = func(*args, **kwargs)
        print('\n\n')
        pp.pprint(output)
        return output
    return Printer


@legoPrinter
def stripe_get_all_disputes(handle) -> Dict:
    """stripe_get_all_disputes Returns a list of disputes that was perviously created. The
        charges are returned in sorted order, with the most recent charges appearing first.
        
        rtype: Returns a list of disputes that was perviously created.
    """

    output = handle.Dispute.list()
    return output