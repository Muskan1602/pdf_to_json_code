# """
# Created on Thu Mon 16 16:39:06 2023
# @author: Muskan Chaudhary
# @description:
# Copyright (C) 2020 LivNSense Technologies - All Rights Reserved
# """
# import json
# import os
# import jwt
# from django.views.decorators.csrf import csrf_exempt
# from cement_api.constants import *
# from supports.response_module import *
# from PyPDF2 import PdfReader
#
#
# # The authentication key (API Key).
# API_KEY = "muskanchaudhary1711@gmail.com_eb5cc265ab91e2ce1202fea2d7515d1bbfe51c0b269a2aff0da128182350ceb9a4e8e230"
#
# # Base URL for PDF.co Web API requests
# BASE_URL = "https://api.pdf_to_json"
#
# # Source PDF file
# SourceFile = "C:\Final_Projects\updated_cement\api\application_interface\RateconKeystone.pdf"
#
# # Comma-separated list of page indices (or ranges) to process. Leave empty for all pages. Example: '0,2-5,7-'.
# Pages = ""
#
# # Destination JSON file name
# DestinationFile = ".\\result.json"
#
# # (!) Make asynchronous job
# Async = True
#
# def main(args = None):
#     uploadedFileUrl = uploadFile(SourceFile)
#     if (uploadedFileUrl != None):
#         convertPdfToJson(uploadedFileUrl, DestinationFile)
#
#
# def pdf_upload(request):
#     if request.method == POST:
#         try:
#             files = request.FILES.getlist('files')
#             if not files:
#                 return JsonResponse({"message": "Attachment not found"}, status=204)
#             else:
#                 for file in files:
#                     print(file)
#                     extension = os.path.splitext(file.name)[1]
#                     print(extension)
#                     if extension == ".pdf":
#                         print(file)
#                         reader = PdfReader(file)
#                         page = reader.pages[0]
#                         page_content = page.extract_text()
#                         # print(page_content)
#                         data = json.dumps(page_content)
#                         # print(data)
#
#                         with open("sample.json", "w") as outfile:
#                             json.dump(data, outfile)
#
#                         with open('sample.json', 'r') as openfile:
#                             json_object = json.load(openfile)
#
#                         print(json_object)
#
#                         dict = {}
#
#                         with open(json_object) as fh:
#                             for line in fh:
#                                 print(line)
#                                 command, description = line.strip().split(None,1)
#                                 dict[command] = description.strip()
#
#                         out_file = open("test1.json", "w")
#                         json.dump(dict, out_file, indent=4, sort_keys=False)
#                         out_file.close()
#
#
#
#                 return response_success({
#                     "message": "Inserted Successfully....."})
#
#         except Exception as err:
#             return response_exception(err)
#         except (jwt.DecodeError, jwt.ExpiredSignatureError):
#             return response_invalid_token()
#
#     else:
#         return response_request_wrong()
#
#
#
#
#
# # If you don't want to pause the main thread you can rework the code
#             # to use a separate thread for the status checking and completion.
#             while True:
#                 status = checkJobStatus(jobId) # Possible statuses: "working", "failed", "aborted", "success".
#                 
#                 # Display timestamp and status (for demo purposes)
#                 print(datetime.datetime.now().strftime("%H:%M.%S") + ": " + status)
#                 
#                 if status == "success":
#                     # Download result file
#                     r = requests.get(resultFileUrl, stream=True)
#                     if (r.status_code == 200):
#                         with open(destinationFile, 'wb') as file:
#                             for chunk in r:
#                                 file.write(chunk)
#                         print(f"Result file saved as \"{destinationFile}\" file.")
#                     else:
#                         print(f"Request error: {response.status_code} {response.reason}")
#                     break
#                 elif status == "working":
#                     # Pause for a few seconds
#                     time.sleep(3)
#                 else:
#                     print(status)
#                     break
#         else:
#             # Show service reported error
#             print(json["message"])
#     else:
#         print(f"Request error: {response.status_code} {response.reason}")
#
#
# def checkJobStatus(jobId):
#     """Checks server job status"""
#
#     url = f"{BASE_URL}/job/check?jobid={jobId}"
#     
#     response = requests.get(url, headers={ "x-api-key": API_KEY })
#     if (response.status_code == 200):
#         json = response.json()
#         return json["status"]
#     else:
#         print(f"Request error: {response.status_code} {response.reason}")
#
#     return None
#
#
# def uploadFile(fileName):
# """Uploads file to the cloud"""
# # 1. RETRIEVE PRESIGNED URL TO UPLOAD FILE.
#
# # Prepare URL for 'Get Presigned URL' API request
# url = "{}/file/upload/get-presigned-url?contenttype=application/octet-stream&name={}".format(
# BASE_URL, os.path.basename(fileName))
# # Execute request and get response as JSON
# response = requests.get(url, headers={ "x-api-key": API_KEY })
# if (response.status_code == 200):
# json = response.json()
#
# if json["error"] == False:
# # URL to use for file upload
# uploadUrl = json["presignedUrl"]
#             # URL for future reference
#             uploadedFileUrl = json["url"]
#
#             # 2. UPLOAD FILE TO CLOUD.
#             with open(fileName, 'rb') as file:
#                 requests.put(uploadUrl, data=file, headers={ "x-api-key": API_KEY, "content-type": "application/octet-stream" })
#
#             return uploadedFileUrl
#         else:
#             # Show service reported error
#             print(json["message"])    
#     else:
#         print(f"Request error: {response.status_code} {response.reason}")
#
#     return None
#
#
# if __name__ == '__main__':
#     main()
#
#
#
#
#
#
#
#
#
#
