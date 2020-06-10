# automatically generated file. DO NOT CHANGE MANUALLY

from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field

from ..... import Kind39, Kind40
from ...apimachinery.pkg.apis.meta import v1


class BoundObjectReference(BaseModel):
    class Config:
        extra = "forbid"

    apiVersion: Optional[str] = Field("v1", description="API version of the referent.")
    kind: Optional[str] = Field(
        None, description="Kind of the referent. Valid kinds are 'Pod' and 'Secret'."
    )
    name: Optional[str] = Field(None, description="Name of the referent.")
    uid: Optional[str] = Field(None, description="UID of the referent.")


class TokenRequestSpec(BaseModel):
    class Config:
        extra = "forbid"

    audiences: List[str] = Field(
        ...,
        description="Audiences are the intendend audiences of the token. A recipient of a token must identitfy themself with an identifier in the list of audiences of the token, and otherwise should reject the token. A token issued for multiple audiences may be used to authenticate against any of the audiences listed but implies a high degree of trust between the target audiences.",
    )
    boundObjectRef: Optional[BoundObjectReference] = Field(
        None,
        description="BoundObjectRef is a reference to an object that the token will be bound to. The token will only be valid for as long as the bound object exists. NOTE: The API server's TokenReview endpoint will validate the BoundObjectRef, but other audiences may not. Keep ExpirationSeconds small if you want prompt revocation.",
    )
    expirationSeconds: Optional[int] = Field(
        None,
        description="ExpirationSeconds is the requested duration of validity of the request. The token issuer may return a token with a different validity duration so a client needs to check the 'expiration' field in a response.",
    )


class TokenReviewSpec(BaseModel):
    class Config:
        extra = "forbid"

    audiences: Optional[List[str]] = Field(
        None,
        description="Audiences is a list of the identifiers that the resource server presented with the token identifies as. Audience-aware token authenticators will verify that the token was intended for at least one of the audiences in this list. If no audiences are provided, the audience will default to the audience of the Kubernetes apiserver.",
    )
    token: Optional[str] = Field(None, description="Token is the opaque bearer token.")


class UserInfo(BaseModel):
    class Config:
        extra = "forbid"

    extra: Optional[Dict[str, Any]] = Field(
        None, description="Any additional information provided by the authenticator."
    )
    groups: Optional[List[str]] = Field(
        None, description="The names of groups this user is a part of."
    )
    uid: Optional[str] = Field(
        None,
        description="A unique value that identifies this user across time. If this user is deleted and another user by the same name is added, they will have different UIDs.",
    )
    username: Optional[str] = Field(
        None,
        description="The name that uniquely identifies this user among all active users.",
    )


class TokenRequestStatus(BaseModel):
    class Config:
        extra = "forbid"

    expirationTimestamp: v1.Time = Field(
        ...,
        description="ExpirationTimestamp is the time of expiration of the returned token.",
    )
    token: str = Field(..., description="Token is the opaque bearer token.")


class TokenReviewStatus(BaseModel):
    class Config:
        extra = "forbid"

    audiences: Optional[List[str]] = Field(
        None,
        description='Audiences are audience identifiers chosen by the authenticator that are compatible with both the TokenReview and token. An identifier is any identifier in the intersection of the TokenReviewSpec audiences and the token\'s audiences. A client of the TokenReview API that sets the spec.audiences field should validate that a compatible audience identifier is returned in the status.audiences field to ensure that the TokenReview server is audience aware. If a TokenReview returns an empty status.audience field where status.authenticated is "true", the token is valid against the audience of the Kubernetes API server.',
    )
    authenticated: Optional[bool] = Field(
        None,
        description="Authenticated indicates that the token was associated with a known user.",
    )
    error: Optional[str] = Field(
        None, description="Error indicates that the token couldn't be checked"
    )
    user: Optional[UserInfo] = Field(
        None, description="User is the UserInfo associated with the provided token."
    )


class TokenRequest(BaseModel):
    class Config:
        extra = "forbid"

    apiVersion: Optional[str] = Field(
        "v1",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[Kind39] = Field(
        "TokenRequest",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ObjectMeta] = None
    spec: TokenRequestSpec
    status: Optional[TokenRequestStatus] = None


class TokenReview(BaseModel):
    class Config:
        extra = "forbid"

    apiVersion: Optional[str] = Field(
        "v1",
        description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
    )
    kind: Optional[Kind40] = Field(
        "TokenReview",
        description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds",
    )
    metadata: Optional[v1.ObjectMeta] = None
    spec: TokenReviewSpec = Field(
        ..., description="Spec holds information about the request being evaluated"
    )
    status: Optional[TokenReviewStatus] = Field(
        None,
        description="Status is filled in by the server and indicates whether the request can be authenticated.",
    )
