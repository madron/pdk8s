# automatically generated file. DO NOT CHANGE MANUALLY

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field

from ..... import Kind55, Kind56
from ...apimachinery.pkg.api import resource
from ...apimachinery.pkg.apis.meta import v1


class CrossVersionObjectReference(BaseModel):
    apiVersion: Optional[str] = Field(
        "v2beta2", description="API version of the referent"
    )
    kind: str = Field(
        ...,
        description='Kind of the referent; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"',
    )
    name: str = Field(
        ...,
        description="Name of the referent; More info: http://kubernetes.io/docs/user-guide/identifiers#names",
    )


class HorizontalPodAutoscalerCondition(BaseModel):
    lastTransitionTime: Optional[v1.Time] = Field(
        None,
        description="lastTransitionTime is the last time the condition transitioned from one status to another",
    )
    message: Optional[str] = Field(
        None,
        description="message is a human-readable explanation containing details about the transition",
    )
    reason: Optional[str] = Field(
        None, description="reason is the reason for the condition's last transition."
    )
    status: str = Field(
        ..., description="status is the status of the condition (True, False, Unknown)"
    )
    type: str = Field(..., description="type describes the current condition")


class MetricTarget(BaseModel):
    averageUtilization: Optional[int] = Field(
        None,
        description="averageUtilization is the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods. Currently only valid for Resource metric source type",
    )
    averageValue: Optional[resource.Quantity] = Field(
        None,
        description="averageValue is the target value of the average of the metric across all relevant pods (as a quantity)",
    )
    type: str = Field(
        ...,
        description="type represents whether the metric type is Utilization, Value, or AverageValue",
    )
    value: Optional[resource.Quantity] = Field(
        None, description="value is the target value of the metric (as a quantity)."
    )


class MetricValueStatus(BaseModel):
    averageUtilization: Optional[int] = Field(
        None,
        description="currentAverageUtilization is the current value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods.",
    )
    averageValue: Optional[resource.Quantity] = Field(
        None,
        description="averageValue is the current value of the average of the metric across all relevant pods (as a quantity)",
    )
    value: Optional[resource.Quantity] = Field(
        None, description="value is the current value of the metric (as a quantity)."
    )


class ResourceMetricSource(BaseModel):
    name: str = Field(..., description="name is the name of the resource in question.")
    target: MetricTarget = Field(
        ..., description="target specifies the target value for the given metric"
    )


class ResourceMetricStatus(BaseModel):
    current: MetricValueStatus = Field(
        ..., description="current contains the current value for the given metric"
    )
    name: str = Field(..., description="Name is the name of the resource in question.")


class MetricIdentifier(BaseModel):
    name: str = Field(..., description="name is the name of the given metric")
    selector: Optional[v1.LabelSelector] = Field(
        None,
        description="selector is the string-encoded form of a standard kubernetes label selector for the given metric When set, it is passed as an additional parameter to the metrics server for more specific metrics scoping. When unset, just the metricName will be used to gather metrics.",
    )


class ObjectMetricSource(BaseModel):
    describedObject: CrossVersionObjectReference
    metric: MetricIdentifier = Field(
        ..., description="metric identifies the target metric by name and selector"
    )
    target: MetricTarget = Field(
        ..., description="target specifies the target value for the given metric"
    )


class ObjectMetricStatus(BaseModel):
    current: MetricValueStatus = Field(
        ..., description="current contains the current value for the given metric"
    )
    describedObject: CrossVersionObjectReference
    metric: MetricIdentifier = Field(
        ..., description="metric identifies the target metric by name and selector"
    )


class PodsMetricSource(BaseModel):
    metric: MetricIdentifier = Field(
        ..., description="metric identifies the target metric by name and selector"
    )
    target: MetricTarget = Field(
        ..., description="target specifies the target value for the given metric"
    )


class PodsMetricStatus(BaseModel):
    current: MetricValueStatus = Field(
        ..., description="current contains the current value for the given metric"
    )
    metric: MetricIdentifier = Field(
        ..., description="metric identifies the target metric by name and selector"
    )


class ExternalMetricSource(BaseModel):
    metric: MetricIdentifier = Field(
        ..., description="metric identifies the target metric by name and selector"
    )
    target: MetricTarget = Field(
        ..., description="target specifies the target value for the given metric"
    )


class ExternalMetricStatus(BaseModel):
    current: MetricValueStatus = Field(
        ..., description="current contains the current value for the given metric"
    )
    metric: MetricIdentifier = Field(
        ..., description="metric identifies the target metric by name and selector"
    )


class MetricSpec(BaseModel):
    external: Optional[ExternalMetricSource] = Field(
        None,
        description="external refers to a global metric that is not associated with any Kubernetes object. It allows autoscaling based on information coming from components running outside of cluster (for example length of queue in cloud messaging service, or QPS from loadbalancer running outside of cluster).",
    )
    object: Optional[ObjectMetricSource] = Field(
        None,
        description="object refers to a metric describing a single kubernetes object (for example, hits-per-second on an Ingress object).",
    )
    pods: Optional[PodsMetricSource] = Field(
        None,
        description="pods refers to a metric describing each pod in the current scale target (for example, transactions-processed-per-second).  The values will be averaged together before being compared to the target value.",
    )
    resource: Optional[ResourceMetricSource] = Field(
        None,
        description='resource refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing each pod in the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source.',
    )
    type: str = Field(
        ...,
        description='type is the type of metric source.  It should be one of "Object", "Pods" or "Resource", each mapping to a matching field in the object.',
    )


class MetricStatus(BaseModel):
    external: Optional[ExternalMetricStatus] = Field(
        None,
        description="external refers to a global metric that is not associated with any Kubernetes object. It allows autoscaling based on information coming from components running outside of cluster (for example length of queue in cloud messaging service, or QPS from loadbalancer running outside of cluster).",
    )
    object: Optional[ObjectMetricStatus] = Field(
        None,
        description="object refers to a metric describing a single kubernetes object (for example, hits-per-second on an Ingress object).",
    )
    pods: Optional[PodsMetricStatus] = Field(
        None,
        description="pods refers to a metric describing each pod in the current scale target (for example, transactions-processed-per-second).  The values will be averaged together before being compared to the target value.",
    )
    resource: Optional[ResourceMetricStatus] = Field(
        None,
        description='resource refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing each pod in the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source.',
    )
    type: str = Field(
        ...,
        description='type is the type of metric source.  It will be one of "Object", "Pods" or "Resource", each corresponds to a matching field in the object.',
    )


class HorizontalPodAutoscalerSpec(BaseModel):
    maxReplicas: int = Field(
        ...,
        description="maxReplicas is the upper limit for the number of replicas to which the autoscaler can scale up. It cannot be less that minReplicas.",
    )
    metrics: Optional[List[MetricSpec]] = Field(
        None,
        description="metrics contains the specifications for which to use to calculate the desired replica count (the maximum replica count across all metrics will be used).  The desired replica count is calculated multiplying the ratio between the target value and the current value by the current number of pods.  Ergo, metrics used must decrease as the pod count is increased, and vice-versa.  See the individual metric source types for more information about how each type of metric must respond. If not set, the default metric will be set to 80% average CPU utilization.",
    )
    minReplicas: Optional[int] = Field(
        None,
        description="minReplicas is the lower limit for the number of replicas to which the autoscaler can scale down.  It defaults to 1 pod.  minReplicas is allowed to be 0 if the alpha feature gate HPAScaleToZero is enabled and at least one Object or External metric is configured.  Scaling is active as long as at least one metric value is available.",
    )
    scaleTargetRef: CrossVersionObjectReference = Field(
        ...,
        description="scaleTargetRef points to the target resource to scale, and is used to the pods for which metrics should be collected, as well as to actually change the replica count.",
    )


class HorizontalPodAutoscalerStatus(BaseModel):
    conditions: List[HorizontalPodAutoscalerCondition] = Field(
        ...,
        description="conditions is the set of conditions required for this autoscaler to scale its target, and indicates whether or not those conditions are met.",
    )
    currentMetrics: Optional[List[MetricStatus]] = Field(
        None,
        description="currentMetrics is the last read state of the metrics used by this autoscaler.",
    )
    currentReplicas: int = Field(
        ...,
        description="currentReplicas is current number of replicas of pods managed by this autoscaler, as last seen by the autoscaler.",
    )
    desiredReplicas: int = Field(
        ...,
        description="desiredReplicas is the desired number of replicas of pods managed by this autoscaler, as last calculated by the autoscaler.",
    )
    lastScaleTime: Optional[v1.Time] = Field(
        None,
        description="lastScaleTime is the last time the HorizontalPodAutoscaler scaled the number of pods, used by the autoscaler to control how often the number of pods is changed.",
    )
    observedGeneration: Optional[int] = Field(
        None,
        description="observedGeneration is the most recent generation observed by this autoscaler.",
    )


class HorizontalPodAutoscaler(BaseModel):
    apiVersion: Optional[str] = Field(
        "v2beta2",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[Kind55] = Field(
        "HorizontalPodAutoscaler",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ObjectMeta] = Field(
        None,
        description="metadata is the standard object metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
    spec: Optional[HorizontalPodAutoscalerSpec] = Field(
        None,
        description="spec is the specification for the behaviour of the autoscaler. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status.",
    )
    status: Optional[HorizontalPodAutoscalerStatus] = Field(
        None, description="status is the current information about the autoscaler."
    )


class HorizontalPodAutoscalerList(BaseModel):
    apiVersion: Optional[str] = Field(
        "v2beta2",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    items: List[HorizontalPodAutoscaler] = Field(
        ..., description="items is the list of horizontal pod autoscaler objects."
    )
    kind: Optional[Kind56] = Field(
        "HorizontalPodAutoscalerList",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ListMeta] = Field(
        None, description="metadata is the standard list metadata."
    )
