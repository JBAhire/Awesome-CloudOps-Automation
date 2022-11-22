##  Copyright (c) 2021 unSkript, Inc
##  All rights reserved.
##
from pydantic import BaseModel, Field
from typing import List, Dict
import pprint

class InputSchema(BaseModel):
    elb_name: str = Field(
        title='ELB Name',
        description='Name of the Load Balancer.')
    instance_ids: List[str] = Field(
        title='Instance IDs',
        description='List of instance IDs. For eg. ["i-foo", "i-bar"]')
    region: str = Field(
        title='Region',
        description='AWS Region of the ELB.')


def aws_deregister_instances_printer(output):
    if output is None:
        return
    pprint.pprint(output)


def aws_deregister_instances(handle, elb_name: str, instance_ids: List, region: str) -> Dict:
    """aws_deregister_instances deregisters instances from a given Load Balancer.
     
        :type handle: object
        :param handle: Object returned by the task.validate(...) method.

        :type elb_name: string
        :param elb_name: Name of the Load Balancer.
        
        :type instance_ids: list
        :param instance_ids: List of instance IDs. For eg. ["i-foo", "i-bar"]
        
        :type region: string
        :param region: AWS Region of the ELB.
        
        :rtype: dict with registered instance details.
    """

    elbClient = handle.client('elb', region_name=region)

    res = elbClient.deregister_instances_from_load_balancer(
        LoadBalancerName=elb_name,
        Instances=[{'InstanceId': instance_id} for instance_id in instance_ids]
    )

    return res