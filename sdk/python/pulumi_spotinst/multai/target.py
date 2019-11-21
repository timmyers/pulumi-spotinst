# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class Target(pulumi.CustomResource):
    balancer_id: pulumi.Output[str]
    """
    The ID of the balancer.
    """
    host: pulumi.Output[str]
    """
    The address (IP or URL) of the targets to register
    """
    name: pulumi.Output[str]
    """
    The name of the Target . Must contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen.
    """
    port: pulumi.Output[float]
    """
    The port the target will register to.
    """
    tags: pulumi.Output[list]
    """
    A list of key:value paired tags.
    
      * `key` (`str`) - The tag's key.
      * `value` (`str`) - The tag's value.
    """
    target_set_id: pulumi.Output[str]
    """
    The ID of the target set.
    """
    weight: pulumi.Output[float]
    """
    Defines how traffic is distributed between targets.
    """
    def __init__(__self__, resource_name, opts=None, balancer_id=None, host=None, name=None, port=None, tags=None, target_set_id=None, weight=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides a Spotinst Multai Target.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] balancer_id: The ID of the balancer.
        :param pulumi.Input[str] host: The address (IP or URL) of the targets to register
        :param pulumi.Input[str] name: The name of the Target . Must contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen.
        :param pulumi.Input[float] port: The port the target will register to.
        :param pulumi.Input[list] tags: A list of key:value paired tags.
        :param pulumi.Input[str] target_set_id: The ID of the target set.
        :param pulumi.Input[float] weight: Defines how traffic is distributed between targets.
        
        The **tags** object supports the following:
        
          * `key` (`pulumi.Input[str]`) - The tag's key.
          * `value` (`pulumi.Input[str]`) - The tag's value.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-spotinst/blob/master/website/docs/r/multai_target.html.markdown.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            if balancer_id is None:
                raise TypeError("Missing required property 'balancer_id'")
            __props__['balancer_id'] = balancer_id
            if host is None:
                raise TypeError("Missing required property 'host'")
            __props__['host'] = host
            __props__['name'] = name
            __props__['port'] = port
            __props__['tags'] = tags
            if target_set_id is None:
                raise TypeError("Missing required property 'target_set_id'")
            __props__['target_set_id'] = target_set_id
            if weight is None:
                raise TypeError("Missing required property 'weight'")
            __props__['weight'] = weight
        super(Target, __self__).__init__(
            'spotinst:multai/target:Target',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, balancer_id=None, host=None, name=None, port=None, tags=None, target_set_id=None, weight=None):
        """
        Get an existing Target resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] balancer_id: The ID of the balancer.
        :param pulumi.Input[str] host: The address (IP or URL) of the targets to register
        :param pulumi.Input[str] name: The name of the Target . Must contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen.
        :param pulumi.Input[float] port: The port the target will register to.
        :param pulumi.Input[list] tags: A list of key:value paired tags.
        :param pulumi.Input[str] target_set_id: The ID of the target set.
        :param pulumi.Input[float] weight: Defines how traffic is distributed between targets.
        
        The **tags** object supports the following:
        
          * `key` (`pulumi.Input[str]`) - The tag's key.
          * `value` (`pulumi.Input[str]`) - The tag's value.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-spotinst/blob/master/website/docs/r/multai_target.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["balancer_id"] = balancer_id
        __props__["host"] = host
        __props__["name"] = name
        __props__["port"] = port
        __props__["tags"] = tags
        __props__["target_set_id"] = target_set_id
        __props__["weight"] = weight
        return Target(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
