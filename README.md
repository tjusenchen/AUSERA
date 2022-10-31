
## AUSERA
AUSERA is an automated tool for detecting security vulnerabilties in Android apps. We have made the tool and the corresponding benchmark dataset publicly available. We hope this project can benefit other researchers or practiontiners in the field of security analysis of Android apps. Please feel free to contact us (senchen@tju.edu.cn) if you have any questions and issues. We will continue to maintain this project. Thanks for your feedback.

## Environment Configuration
* Ubuntu/Macbook
* Python: (both 2 and 3 should be fine)
* APKTool: 2.6.1 (Please use the newest version of APKTool), ref: [ApkTool Install Instructions](https://ibotpeaches.github.io/Apktool/install/)
* Java environment (jdk): jdk1.8.0_45 `export JAVA_HOME=/usr/lib/jvm/jdk1.8.0_45` Install android SDK, ref: [sdkmanager](https://developer.android.com/studio/command-line/sdkmanager). On mac,  the sdks will be saved in `~/Library/Android/sdk/platforms`
* Open ~/.bashrc and configure the path of JDK and SDK (Replace by your own paths):
```
export JAVA_HOME=/usr/lib/jvm/jdk1.8.0_45
export JAVA_BIN=/usr/lib/jvm/jdk1.8.0_45/bin
export CLASSPATH=.:${JAVA_HOME}/lib/dt.jar:${JAVA_HOME}/lib/tools.jar
export PATH=$PATH:${JAVA_HOME}/bin
export PATH=$PATH:/home/dell/Android/Sdk/tools
export PATH=$PATH:/home/dell/Android/Sdk/platform-tools
export PATH=$PATH:/home/dell/Android/Sdk/emulator
export JAVA_HOME JAVA_BIN CLASSPATH PATH 
```

## Execution Record
https://youtu.be/sfUK3b3IuEU

## Usage

> Please put target apk file under test to `apks` folder
> 
> output report can be found in `engine-result/engine-report/apk_sha256_output.json`

**Command format:**

`python apk-engine.py [Repo_Path] [JAVA_HOME_Path] [SDK_Platform_Path]`


**Example:**

`python2.7 apk-engine.py /media/dell/49fff1d2-ef19-4e4d-855b-4eca95be873a/dell/Tools/ausera-main/ /usr/lib/jvm/jdk1.8.0_45/ /media/dell/49fff1d2-ef19-4e4d-855b-4eca95be873a/dell/Tools/ausera-main/engine-configuration/libs/android-platforms/`

## Output
```
Public Id: BUG-A003-0001; 
Type: Security Bug; 
Risk Level: High; 
Risk Score: 8;
Sub Type: SMS data leakage; // App vulnerability type
Description: The app sends an SMS attached with the sensitive data (in plaintext) to authenticate that user, but the data is stored in the SMS outbox unexpectedly. If an adversary registers a content observer to the SMS outbox on the mobile device with some permissions, the user's sensitive data can be easily intercepted by the adversary who impersonates that user to manipulate her legitimate banking account.
Location: Found a flow to sink virtualinvoke $r10.<android.telephony.SmsManager: void sendTextMessage(), from the following sources: $r5 = virtualinvoke $r4.<android.widget.EditText: android.text.Editable getText()>() (in <com.globe.gcash.android.activity.transaction.RegistrationTransactionActivity: void doNext()>) 
=> RegistrationTransactionActivity;doNext();$r4;$r5 // Activity, Method, Variables logging
==> pin;firstName;lastName;addr // Sensitive data tagging
Patch Method: Avoid sending sensitive data via SMS and store the sensitive data in the SMS outbox accordingly.
```

## Papers


[1] AUSERA: Automated Security Risk Assessment for Vulnerability Detection in Android Apps
```
@inproceedings{chen2022ausera,
  title={AUSERA: Automated Security Risk Assessment for Vulnerability Detection in Android Apps},
  author={Chen, Sen and and Zhang, Yuxin and Fan, Lingling and Li, Jiaming and Liu, Yang},
  booktitle={ASE},
  year={2022}
}
```

[2] An Empirical Assessment of Security Risks of Global Android Banking Apps
```
@inproceedings{chen2019ausera,
  title={An Empirical Assessment of Security Risks of Global {Android} Banking Apps},
  author={Chen, Sen and Fan, Lingling and Meng, Guozhu and Su, Ting and Xue, Minhui and Xue, Yinxing and Liu, Yang and Xu, Lihua},
  booktitle={ICSE},
  year={2020}
}
```

[3] Are Mobile Banking Apps Secure? What Can be Improved?
```
@inproceedings{chen2018mobile,
  title={Are mobile banking apps secure? {What} can be improved?},
  author={Chen, Sen and Su, Ting and Fan, Lingling and Meng, Guozhu and Xue, Minhui and Liu, Yang and Xu, Lihua},
  booktitle={ESEC/FSE},
  year={2018}
}
```

## Contact
[Sen Chen](https://sen-chen.github.io/) All Copyright Reserved.
