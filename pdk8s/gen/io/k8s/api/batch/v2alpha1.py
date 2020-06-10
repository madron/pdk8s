# automatically generated file. DO NOT CHANGE MANUALLY

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field

from ..... import Kind61, Kind62
from ...apimachinery.pkg.apis.meta import v1 as v1_1
from ..core import v1
from . import v1 as v1_1


class CronJobStatus(BaseModel):
    class Config:
        extra = "forbid"

    active: Optional[List[v1.ObjectReference]] = Field(
        None, description="A list of pointers to currently running jobs."
    )
    lastScheduleTime: Optional[v1_1.Time] = Field(
        None,
        description="Information when was the last time the job was successfully scheduled.",
    )


class JobTemplateSpec(BaseModel):
    class Config:
        extra = "forbid"

    metadata: Optional[v1.ObjectMeta] = Field(
        None,
        description="Standard object's metadata of the jobs created from this template. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
    spec: Optional[v1_1.JobSpec] = Field(
        None,
        description="Specification of the desired behavior of the job. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status",
    )


class CronJobSpec(BaseModel):
    class Config:
        extra = "forbid"

    concurrencyPolicy: Optional[str] = Field(
        None,
        description='Specifies how to treat concurrent executions of a Job. Valid values are: - "Allow" (default): allows CronJobs to run concurrently; - "Forbid": forbids concurrent runs, skipping next run if previous run hasn\'t finished yet; - "Replace": cancels currently running job and replaces it with a new one',
    )
    failedJobsHistoryLimit: Optional[int] = Field(
        None,
        description="The number of failed finished jobs to retain. This is a pointer to distinguish between explicit zero and not specified.",
    )
    jobTemplate: JobTemplateSpec = Field(
        ...,
        description="Specifies the job that will be created when executing a CronJob.",
    )
    schedule: str = Field(
        ...,
        description="The schedule in Cron format, see https://en.wikipedia.org/wiki/Cron.",
    )
    startingDeadlineSeconds: Optional[int] = Field(
        None,
        description="Optional deadline in seconds for starting the job if it misses scheduled time for any reason.  Missed jobs executions will be counted as failed ones.",
    )
    successfulJobsHistoryLimit: Optional[int] = Field(
        None,
        description="The number of successful finished jobs to retain. This is a pointer to distinguish between explicit zero and not specified.",
    )
    suspend: Optional[bool] = Field(
        None,
        description="This flag tells the controller to suspend subsequent executions, it does not apply to already started executions.  Defaults to false.",
    )


class CronJob(BaseModel):
    class Config:
        extra = "forbid"

    apiVersion: Optional[str] = Field(
        "v2alpha1",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[Kind61] = Field(
        "CronJob",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ObjectMeta] = Field(
        None,
        description="Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
    spec: Optional[CronJobSpec] = Field(
        None,
        description="Specification of the desired behavior of a cron job, including the schedule. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status",
    )
    status: Optional[CronJobStatus] = Field(
        None,
        description="Current status of a cron job. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status",
    )


class CronJobList(BaseModel):
    class Config:
        extra = "forbid"

    apiVersion: Optional[str] = Field(
        "v2alpha1",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    items: List[CronJob] = Field(..., description="items is the list of CronJobs.")
    kind: Optional[Kind62] = Field(
        "CronJobList",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description="Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
