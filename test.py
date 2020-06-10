#!/user/bin/env python3
# coding=utf-8
'''
@project : project_test
@author  : anton Wang
@file   : test.py
@IDE   : PyCharm
@date  : 2020-03-17
'''
import json

# names = ["q", "w", "e"]
# # ages = [12, 13, 14]
# # add = ["x", "c", "v"]
# # len = names.__len__()
# # res = []
# # for i in range(0, len):
# #     item = {
# #         "name":names[i],
# #         "age":ages[i],
# #         "add":add[i]
# #     }
# #     res.append(item)
# # print(res)


# make sure ES is up and running
# res = requests.get('http://172.31.3.50:9200')
# print(res.content)
# li = [1,2,3,4,5]
# x = map(lambda x: x + 1, li)
# print(x)

s = "djfjsgnksemlkgmlew"
print(s[:1])
test = [i for i in s]
print(test)

j = {
  "deptName": "",
  "certType": "身份证号",
  "guardianGender": "",
  "bizCode": "",
  "companyName": "",
  "phoneNum": "",
  "guardianIdNo": "",
  "diseaseList": [
    {
      "code": "",
      "icd": "",
      "name": "139.0",
      "description": "股骨头损伤0",
      "sort": "0",
      "inHosDiagnoseType": "0",
      "treatmentOutcome": "治疗结果：病人脱离生命危险，情况逐步好转"
    },
     {
      "code": "",
      "icd": "",
      "name": "139.1",
      "description": "股骨头损伤1",
      "sort": "0",
      "inHosDiagnoseType": "1",
      "treatmentOutcome": "治疗结果：病人脱离生命危险，情况逐步好转"
    },
    {
      "code": "",
      "icd": "",
      "name": "139.2",
      "description": "股骨头损伤2",
      "sort": "0",
      "inHosDiagnoseType": "2",
      "treatmentOutcome": "治疗结果：病人脱离生命危险，情况逐步好转"
    }
  ],
  "historyPresentIllness": "现病史：股骨头坏死，需要接受手术。",
  "diagnosisTreatment": "",
  "medicalAbstract": "",
  "physicalExamination": "",
  "ageUnit": "",
  "medicalNum": "test001",
  "pastDiseaseHistory": "既往史：未患既往病史",
  "hospitalizationDays": "",
  "cheifComplaint": "主诉：股骨头损伤",
  "medicalBillingExist": "",
  "reportNo": "",
  "homeAddress": "",
  "departmentName": "",
  "medicationRecommendations": "",
  "format": "",
  "linkmanName": "",
  "certNo": "350101012121",
  "visitTime": "",
  "hospitalRecordType": "门诊",
  "name": "王强",
  "outPatientNum": "emr001",
  "juniorCollege": "",
  "menstruationHistory": "月经史：无",
  "treatmentInfo": "",
  "birthday": "",
  "gender": "男",
  "conditionInHospital": "",
  "dischargeStatus": "",
  "admissionName": "",
  "linkmanMobile": "",
  "hospitalCode": "testorgcode",
  "obstetricalHistory": "婚育史：已婚，配偶健康，现有一子，身体健康",
  "operationList": [
    {
      "departmentName": "",
      "operationDate": "手术时间：2019年1月16号",
      "operationCode": "",
      "operationName": "手术名称：股骨头重建术",
      "operationSite": "",
      "operationLevelName": "",
      "operationIncisionCategory": "",
      "anesthesiaMethodName": "",
      "doctorName": "",
      "assistantDoctorName": "",
      "preoperativeDiagnosis": "",
      "intraoperativeDiagnosis": "",
      "operationProcess": "",
      "totalOperationRecordInfo": ""
    }
  ],
  "bizMsg": "",
  "guardianName": "",
  "totalRecordInfo": "",
  "familyHistory": "家族史：否认家族遗传疾病及相关病史",
  "email": "",
  "dischargeTime": "",
  "race": "汉",
  "relationshipOfPatient": "",
  "specialDiseases": "",
  "hospitalRecordId": "emr00101",
  "guardianIdType": "",
  "inHospitalNum": "test001",
  "clinicalPath": "",
  "guardianBirthday": "",
  "attendingPhysician": "aaa",
  "personalHistory": "个人史：无不良嗜好",
  "businessTransaction": "",
  "auxiliaryExamination": "",
  "businessType": "",
  "mainTestResults": "",
  "age": "20"
}
x = json.dumps(j,ensure_ascii=False)
print(x)

z = ['11', 2, None, "assfua", "dshfu", 2, None]
while None in z:
    print("remove none")
    z.remove(None)
print(z)
