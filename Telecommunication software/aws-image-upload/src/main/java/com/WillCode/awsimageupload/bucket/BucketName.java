package com.WillCode.awsimageupload.bucket;

public enum BucketName {
    PROFILE_IMAGE("Mycode-image-upload-XDnot_thereal_one");

    private final String bucketName;

    BucketName(String bucketName) {
        this.bucketName = bucketName;
    }

    public String getBucketName() {
        return bucketName;
    }
}
