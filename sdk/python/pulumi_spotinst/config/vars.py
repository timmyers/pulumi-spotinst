# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

__config__ = pulumi.Config('spotinst')

account = __config__.get('account') or (utilities.get_env('SPOTINST_ACCOUNT') or '')
"""
Spotinst Account ID
"""

token = __config__.get('token') or (utilities.get_env('SPOTINST_TOKEN') or '')
"""
Spotinst Personal API Access Token
"""

