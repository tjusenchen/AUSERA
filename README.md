## Requirement
1. python (both 2 and 3 should be fine)

2. JDK installed eg.: `export JAVA_HOME=/usr/lib/jvm/jdk1.8.0_45`

3. Install ApkTool, ref: [ApkTool Install Instructions](https://ibotpeaches.github.io/Apktool/install/)

4. install android SDK, ref: [sdkmanager](https://developer.android.com/studio/command-line/sdkmanager). On mac,  the sdks will be saved in `~/Library/Android/sdk/platforms`

## How to run
> !! put target apk file to `apks` folder
> 
> output report can be found in `engine-result/engine-report/apk_sha256_output.txt`

**Command format:**

`python apk-engine.py [Repo_Path] [JAVA_HOME_Path] [SDK_Platform_Path]`


**Example:**

`python apk-engine.py /Users/turly221/PycharmProjects/apk_engine_repo /Users/turly221/.jenv/versions/openjdk64-1.8.0.242 /Users/turly221/Library/Android/sdk/platforms`


## Contact
[Sen Chen](https://sen-chen.github.io/) All Copyright Reserved.
