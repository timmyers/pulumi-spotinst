// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-spotinst/blob/master/website/docs/r/elastigroup_gke.html.markdown.
 */
export class Elastigroup extends pulumi.CustomResource {
    /**
     * Get an existing Elastigroup resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ElastigroupState, opts?: pulumi.CustomResourceOptions): Elastigroup {
        return new Elastigroup(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'spotinst:gke/elastigroup:Elastigroup';

    /**
     * Returns true if the given object is an instance of Elastigroup.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Elastigroup {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Elastigroup.__pulumiType;
    }

    public readonly backendServices!: pulumi.Output<outputs.gke.ElastigroupBackendService[] | undefined>;
    /**
     * The name of the GKE cluster you wish to import.
     */
    public readonly clusterId!: pulumi.Output<string | undefined>;
    /**
     * The zone where the cluster is hosted.
     */
    public readonly clusterZoneName!: pulumi.Output<string>;
    public readonly desiredCapacity!: pulumi.Output<number>;
    public readonly disks!: pulumi.Output<outputs.gke.ElastigroupDisk[] | undefined>;
    public readonly drainingTimeout!: pulumi.Output<number | undefined>;
    public readonly fallbackToOndemand!: pulumi.Output<boolean | undefined>;
    public readonly gpu!: pulumi.Output<outputs.gke.ElastigroupGpu[] | undefined>;
    public readonly instanceTypesCustoms!: pulumi.Output<outputs.gke.ElastigroupInstanceTypesCustom[] | undefined>;
    public readonly instanceTypesOndemand!: pulumi.Output<string | undefined>;
    public readonly instanceTypesPreemptibles!: pulumi.Output<string[] | undefined>;
    public readonly integrationDockerSwarm!: pulumi.Output<outputs.gke.ElastigroupIntegrationDockerSwarm | undefined>;
    public readonly integrationGke!: pulumi.Output<outputs.gke.ElastigroupIntegrationGke | undefined>;
    public readonly ipForwarding!: pulumi.Output<boolean | undefined>;
    public readonly labels!: pulumi.Output<outputs.gke.ElastigroupLabel[] | undefined>;
    public readonly maxSize!: pulumi.Output<number>;
    public readonly metadatas!: pulumi.Output<outputs.gke.ElastigroupMetadata[] | undefined>;
    public readonly minSize!: pulumi.Output<number>;
    public readonly name!: pulumi.Output<string>;
    public readonly networkInterfaces!: pulumi.Output<outputs.gke.ElastigroupNetworkInterface[] | undefined>;
    /**
     * The image that will be used for the node VMs. Possible values: COS, UBUNTU.
     */
    public readonly nodeImage!: pulumi.Output<string | undefined>;
    public readonly ondemandCount!: pulumi.Output<number | undefined>;
    public readonly preemptiblePercentage!: pulumi.Output<number | undefined>;
    public readonly scalingDownPolicies!: pulumi.Output<outputs.gke.ElastigroupScalingDownPolicy[] | undefined>;
    public readonly scalingUpPolicies!: pulumi.Output<outputs.gke.ElastigroupScalingUpPolicy[] | undefined>;
    public readonly serviceAccount!: pulumi.Output<string | undefined>;
    public readonly shutdownScript!: pulumi.Output<string | undefined>;
    public readonly startupScript!: pulumi.Output<string | undefined>;
    public readonly tags!: pulumi.Output<string[] | undefined>;

    /**
     * Create a Elastigroup resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ElastigroupArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ElastigroupArgs | ElastigroupState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as ElastigroupState | undefined;
            inputs["backendServices"] = state ? state.backendServices : undefined;
            inputs["clusterId"] = state ? state.clusterId : undefined;
            inputs["clusterZoneName"] = state ? state.clusterZoneName : undefined;
            inputs["desiredCapacity"] = state ? state.desiredCapacity : undefined;
            inputs["disks"] = state ? state.disks : undefined;
            inputs["drainingTimeout"] = state ? state.drainingTimeout : undefined;
            inputs["fallbackToOndemand"] = state ? state.fallbackToOndemand : undefined;
            inputs["gpu"] = state ? state.gpu : undefined;
            inputs["instanceTypesCustoms"] = state ? state.instanceTypesCustoms : undefined;
            inputs["instanceTypesOndemand"] = state ? state.instanceTypesOndemand : undefined;
            inputs["instanceTypesPreemptibles"] = state ? state.instanceTypesPreemptibles : undefined;
            inputs["integrationDockerSwarm"] = state ? state.integrationDockerSwarm : undefined;
            inputs["integrationGke"] = state ? state.integrationGke : undefined;
            inputs["ipForwarding"] = state ? state.ipForwarding : undefined;
            inputs["labels"] = state ? state.labels : undefined;
            inputs["maxSize"] = state ? state.maxSize : undefined;
            inputs["metadatas"] = state ? state.metadatas : undefined;
            inputs["minSize"] = state ? state.minSize : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["networkInterfaces"] = state ? state.networkInterfaces : undefined;
            inputs["nodeImage"] = state ? state.nodeImage : undefined;
            inputs["ondemandCount"] = state ? state.ondemandCount : undefined;
            inputs["preemptiblePercentage"] = state ? state.preemptiblePercentage : undefined;
            inputs["scalingDownPolicies"] = state ? state.scalingDownPolicies : undefined;
            inputs["scalingUpPolicies"] = state ? state.scalingUpPolicies : undefined;
            inputs["serviceAccount"] = state ? state.serviceAccount : undefined;
            inputs["shutdownScript"] = state ? state.shutdownScript : undefined;
            inputs["startupScript"] = state ? state.startupScript : undefined;
            inputs["tags"] = state ? state.tags : undefined;
        } else {
            const args = argsOrState as ElastigroupArgs | undefined;
            if (!args || args.clusterZoneName === undefined) {
                throw new Error("Missing required property 'clusterZoneName'");
            }
            if (!args || args.desiredCapacity === undefined) {
                throw new Error("Missing required property 'desiredCapacity'");
            }
            inputs["backendServices"] = args ? args.backendServices : undefined;
            inputs["clusterId"] = args ? args.clusterId : undefined;
            inputs["clusterZoneName"] = args ? args.clusterZoneName : undefined;
            inputs["desiredCapacity"] = args ? args.desiredCapacity : undefined;
            inputs["disks"] = args ? args.disks : undefined;
            inputs["drainingTimeout"] = args ? args.drainingTimeout : undefined;
            inputs["fallbackToOndemand"] = args ? args.fallbackToOndemand : undefined;
            inputs["gpu"] = args ? args.gpu : undefined;
            inputs["instanceTypesCustoms"] = args ? args.instanceTypesCustoms : undefined;
            inputs["instanceTypesOndemand"] = args ? args.instanceTypesOndemand : undefined;
            inputs["instanceTypesPreemptibles"] = args ? args.instanceTypesPreemptibles : undefined;
            inputs["integrationDockerSwarm"] = args ? args.integrationDockerSwarm : undefined;
            inputs["integrationGke"] = args ? args.integrationGke : undefined;
            inputs["ipForwarding"] = args ? args.ipForwarding : undefined;
            inputs["labels"] = args ? args.labels : undefined;
            inputs["maxSize"] = args ? args.maxSize : undefined;
            inputs["metadatas"] = args ? args.metadatas : undefined;
            inputs["minSize"] = args ? args.minSize : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["networkInterfaces"] = args ? args.networkInterfaces : undefined;
            inputs["nodeImage"] = args ? args.nodeImage : undefined;
            inputs["ondemandCount"] = args ? args.ondemandCount : undefined;
            inputs["preemptiblePercentage"] = args ? args.preemptiblePercentage : undefined;
            inputs["scalingDownPolicies"] = args ? args.scalingDownPolicies : undefined;
            inputs["scalingUpPolicies"] = args ? args.scalingUpPolicies : undefined;
            inputs["serviceAccount"] = args ? args.serviceAccount : undefined;
            inputs["shutdownScript"] = args ? args.shutdownScript : undefined;
            inputs["startupScript"] = args ? args.startupScript : undefined;
            inputs["tags"] = args ? args.tags : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(Elastigroup.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Elastigroup resources.
 */
export interface ElastigroupState {
    readonly backendServices?: pulumi.Input<pulumi.Input<inputs.gke.ElastigroupBackendService>[]>;
    /**
     * The name of the GKE cluster you wish to import.
     */
    readonly clusterId?: pulumi.Input<string>;
    /**
     * The zone where the cluster is hosted.
     */
    readonly clusterZoneName?: pulumi.Input<string>;
    readonly desiredCapacity?: pulumi.Input<number>;
    readonly disks?: pulumi.Input<pulumi.Input<inputs.gke.ElastigroupDisk>[]>;
    readonly drainingTimeout?: pulumi.Input<number>;
    readonly fallbackToOndemand?: pulumi.Input<boolean>;
    readonly gpu?: pulumi.Input<pulumi.Input<inputs.gke.ElastigroupGpu>[]>;
    readonly instanceTypesCustoms?: pulumi.Input<pulumi.Input<inputs.gke.ElastigroupInstanceTypesCustom>[]>;
    readonly instanceTypesOndemand?: pulumi.Input<string>;
    readonly instanceTypesPreemptibles?: pulumi.Input<pulumi.Input<string>[]>;
    readonly integrationDockerSwarm?: pulumi.Input<inputs.gke.ElastigroupIntegrationDockerSwarm>;
    readonly integrationGke?: pulumi.Input<inputs.gke.ElastigroupIntegrationGke>;
    readonly ipForwarding?: pulumi.Input<boolean>;
    readonly labels?: pulumi.Input<pulumi.Input<inputs.gke.ElastigroupLabel>[]>;
    readonly maxSize?: pulumi.Input<number>;
    readonly metadatas?: pulumi.Input<pulumi.Input<inputs.gke.ElastigroupMetadata>[]>;
    readonly minSize?: pulumi.Input<number>;
    readonly name?: pulumi.Input<string>;
    readonly networkInterfaces?: pulumi.Input<pulumi.Input<inputs.gke.ElastigroupNetworkInterface>[]>;
    /**
     * The image that will be used for the node VMs. Possible values: COS, UBUNTU.
     */
    readonly nodeImage?: pulumi.Input<string>;
    readonly ondemandCount?: pulumi.Input<number>;
    readonly preemptiblePercentage?: pulumi.Input<number>;
    readonly scalingDownPolicies?: pulumi.Input<pulumi.Input<inputs.gke.ElastigroupScalingDownPolicy>[]>;
    readonly scalingUpPolicies?: pulumi.Input<pulumi.Input<inputs.gke.ElastigroupScalingUpPolicy>[]>;
    readonly serviceAccount?: pulumi.Input<string>;
    readonly shutdownScript?: pulumi.Input<string>;
    readonly startupScript?: pulumi.Input<string>;
    readonly tags?: pulumi.Input<pulumi.Input<string>[]>;
}

/**
 * The set of arguments for constructing a Elastigroup resource.
 */
export interface ElastigroupArgs {
    readonly backendServices?: pulumi.Input<pulumi.Input<inputs.gke.ElastigroupBackendService>[]>;
    /**
     * The name of the GKE cluster you wish to import.
     */
    readonly clusterId?: pulumi.Input<string>;
    /**
     * The zone where the cluster is hosted.
     */
    readonly clusterZoneName: pulumi.Input<string>;
    readonly desiredCapacity: pulumi.Input<number>;
    readonly disks?: pulumi.Input<pulumi.Input<inputs.gke.ElastigroupDisk>[]>;
    readonly drainingTimeout?: pulumi.Input<number>;
    readonly fallbackToOndemand?: pulumi.Input<boolean>;
    readonly gpu?: pulumi.Input<pulumi.Input<inputs.gke.ElastigroupGpu>[]>;
    readonly instanceTypesCustoms?: pulumi.Input<pulumi.Input<inputs.gke.ElastigroupInstanceTypesCustom>[]>;
    readonly instanceTypesOndemand?: pulumi.Input<string>;
    readonly instanceTypesPreemptibles?: pulumi.Input<pulumi.Input<string>[]>;
    readonly integrationDockerSwarm?: pulumi.Input<inputs.gke.ElastigroupIntegrationDockerSwarm>;
    readonly integrationGke?: pulumi.Input<inputs.gke.ElastigroupIntegrationGke>;
    readonly ipForwarding?: pulumi.Input<boolean>;
    readonly labels?: pulumi.Input<pulumi.Input<inputs.gke.ElastigroupLabel>[]>;
    readonly maxSize?: pulumi.Input<number>;
    readonly metadatas?: pulumi.Input<pulumi.Input<inputs.gke.ElastigroupMetadata>[]>;
    readonly minSize?: pulumi.Input<number>;
    readonly name?: pulumi.Input<string>;
    readonly networkInterfaces?: pulumi.Input<pulumi.Input<inputs.gke.ElastigroupNetworkInterface>[]>;
    /**
     * The image that will be used for the node VMs. Possible values: COS, UBUNTU.
     */
    readonly nodeImage?: pulumi.Input<string>;
    readonly ondemandCount?: pulumi.Input<number>;
    readonly preemptiblePercentage?: pulumi.Input<number>;
    readonly scalingDownPolicies?: pulumi.Input<pulumi.Input<inputs.gke.ElastigroupScalingDownPolicy>[]>;
    readonly scalingUpPolicies?: pulumi.Input<pulumi.Input<inputs.gke.ElastigroupScalingUpPolicy>[]>;
    readonly serviceAccount?: pulumi.Input<string>;
    readonly shutdownScript?: pulumi.Input<string>;
    readonly startupScript?: pulumi.Input<string>;
    readonly tags?: pulumi.Input<pulumi.Input<string>[]>;
}
