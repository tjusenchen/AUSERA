#!/usr/bin/env python
#coding:utf-8

import os
import sys
import commands
import hashlib

def endWith(s, *endstring):
    array = map(s.endswith, endstring)
    if True in array:
        return True
    else:
        return False

def run_json_format(json_jar, report_url, apk_engine_report, apk, apk_sha256, apks_path):
    apk_name = apk.rstrip('.apk')
    report = open(report_url, 'a')
    report.write('\nAPK engine finished on')
    print 'initial report: ' + report_url
    print 'report path: ' + apk_engine_report
    print 'apk name: ' + apk_name
    print 'apk sha256 ' + apk_sha256
    print "java -jar %s %s %s %s %s"%(json_jar, report_url, apk_engine_report, apk_name, apk_sha256)
    os.system("java -jar %s %s %s %s %s"%(json_jar, report_url, apk_engine_report, apk_name, apk_sha256))
    print 'json parse done'
    if(os.path.exists(os.path.join(apks_path,apk_sha256+".apk"))):
        os.remove(os.path.join(apks_path,apk_sha256+".apk"))  # Delete the apk
    if(os.path.exists(os.path.join(apks_path, apk_name + ".apk"))):
        os.remove(os.path.join(apks_path,apk_name + ".apk"))

def main():
    len(sys.argv)
    environment_apk_engine = sys.argv[1]
    apks_path = environment_apk_engine + "/apks/"
    jdk_version = sys.argv[2]
    sdk_path = sys.argv[3]
    os.chdir(apks_path)
    apk_engine_result = environment_apk_engine + "/engine-result"
    apk_engine_report = apk_engine_result + "/engine-report"
    apk_engine_config = environment_apk_engine + '/engine-configuration'
    apk_engine_rename_jar = apk_engine_config + '/ReName.jar'
    apk_engine_config_jar = apk_engine_config + '/Config.jar'
    apk_engine_jar = apk_engine_config + '/APKEngine.jar'
    apk_engine_flowdroid_jar = apk_engine_config + '/FlowDroid.jar'
    #apk_engine_flowdroid_android_platform = apk_engine_config + "/libs/android-platforms/"
    apk_engine_flowdroid_android_platform = sdk_path
    apk_engine_iccta_jar = apk_engine_config + '/IccTA.jar'
    #apk_engine_iccta_android_jar = apk_engine_config + "/libs/android-platforms/android-22/android.jar"
    apk_engine_iccta_android_jar = sdk_path + "/android-22/android.jar"
    apk_engine_json_jar = apk_engine_config + '/Json.jar'
    if not os.path.exists(apk_engine_result):
        os.system("java -jar " + apk_engine_config_jar + " " + environment_apk_engine)
    first_file = apk_engine_result + "/run(Engine)_report.txt"
    flowdroid_file = apk_engine_result + "/run(Flowdroid)_report.txt"
    iccta_file = apk_engine_result + "/run(IccTA)_report.txt"
    if not (os.path.exists(first_file)):
        os.mknod(first_file)
    if not (os.path.exists(flowdroid_file)):
        os.mknod(flowdroid_file)
    if not (os.path.exists(iccta_file)):
        os.mknod(iccta_file)
    apks = os.listdir(apks_path)
    for apk in apks:
        if endWith(apk, '.apk'):
            apk_sha256 = commands.getoutput("sha256sum " + apk).split(" ")[0]
            apk_sha256_txt = apk_sha256 + '.txt'
            report_url = os.path.join(apk_engine_report, apk_sha256_txt)

            if (os.system("java -jar " + apk_engine_flowdroid_jar + " " + apk + " " + apk_engine_flowdroid_android_platform + " "
                + environment_apk_engine + " " + jdk_version)):
                with open(flowdroid_file, "ab") as flowdroid:
                    flowdroid.write(apk + ": fail(Flowdroid)" + "\n")
            else:
                with open(flowdroid_file, "ab") as flowdroid:
                    flowdroid.write(apk + ": succeed(Flowdroid)" + "\n")
            if (os.system("java -jar " + apk_engine_iccta_jar + " " + apk + " " + apk_engine_iccta_android_jar + " "
                + environment_apk_engine + " " + jdk_version)):
                with open(iccta_file, "ab") as iccta:
                    iccta.write(apk + ": fail(IccTA)" + "\n")
            else:
                with open(iccta_file, "ab") as iccta:
                    iccta.write(apk + ": succeed(IccTA)" + "\n")
            '''
            if (os.system("java -jar " + apk_engine_jar + " " + apk + " " + environment_apk_engine + " " + jdk_version + " " + sdk_path)):
                with open(first_file, "ab") as first:
                    first.write(apk + ": fail(APKEngine)" + "\n")
                    run_json_format(apk_engine_json_jar, report_url, apk_engine_report, apk, apk_sha256, apks_path)
            '''
            os.chdir(apk_engine_config)
            if (os.system("./run-engine.run" + " " + apk + " " + environment_apk_engine + " " + jdk_version + " " + sdk_path)):
                with open(first_file, "ab") as first:
                    first.write(apk + ": fail(APKEngine)" + "\n")
                    run_json_format(apk_engine_json_jar, report_url, apk_engine_report, apk, apk_sha256, apks_path)

            else:
                with open(first_file, "ab") as first:
                    first.write(apk + ": succeed(APKEngine)" + "\n")

if __name__ == '__main__':
    main()
    #run_json_format("/home/senchen/Desktop/apk_engine/engine-configuration/Json.jar",
                    #"/home/senchen/Desktop/apk_engine/engine-result/engine-report/4154ed28980535f775ca34a8dd805b534affb3a4a4fc70cadda63713eb05816a.txt",
                    #"/home/senchen/Desktop/apk_engine/engine-result/engine-report",
                    #"/home/senchen/Desktop/apk_engine/apks/4154ed28980535f775ca34a8dd805b534affb3a4a4fc70cadda63713eb05816a.apk",
                    #"4154ed28980535f775ca34a8dd805b534affb3a4a4fc70cadda63713eb05816a")