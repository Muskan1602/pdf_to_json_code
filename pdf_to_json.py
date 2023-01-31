import os
import requests

# The authentication key (API Key).
API_KEY = "muskanchaudhary1711@gmail.com_eb5cc265ab91e2ce1202fea2d7515d1bbfe51c0b269a2aff0da128182350ceb9a4e8e230"

# Base URL for PDF.co Web API requests
BASE_URL = "https://api.pdf.co/v1"

# Source PDF file
SourceFile = ".\\RateconKeystone.pdf"

# Comma-separated list of page indices (or ranges) to process.
Pages = ""

# Destination JSON file name
DestinationFile = ".\\result.json"


def main(args = None):
    uploadedFileUrl = uploadFile(SourceFile)
    if (uploadedFileUrl != None):
        convertPdfToJson(uploadedFileUrl, DestinationFile)


def convertPdfToJson(uploadedFileUrl, destinationFile):
    """Converts PDF To Json using PDF.co Web API"""
    parameters = {}
    parameters["name"] = os.path.basename(destinationFile)
    parameters["pages"] = Pages
    parameters["url"] = uploadedFileUrl

    # Prepare URL for 'PDF To Json' API request
    url = "{}/pdf/convert/to/json".format(BASE_URL)
    # print(url)

    # Execute request and get response as JSON
    response = requests.post(url, data=parameters, headers={"x-api-key": API_KEY})
    if (response.status_code == 200):
        json = response.json()

        if json["error"] == False:
            #  Get URL of result file
            resultFileUrl = json["url"]
            # Download result file
            r = requests.get(resultFileUrl, stream=True)
            if (r.status_code == 200):
                with open(destinationFile, 'wb') as file:
                    for chunk in r:
                        file.write(chunk)

                print(f"Result file saved as \"{destinationFile}\" file.")
            else:
                print(f"Request error: {response.status_code} {response.reason}")
        else:
            # Show service reported error
            print(json["message"])
    else:
        print(f"Request error: {response.status_code} {response.reason}")


def uploadFile(fileName):
    """Uploads file to the cloud"""

    url = "{}/file/upload/get-presigned-url?contenttype=application/json&name={}".format(BASE_URL, os.path.basename(fileName))
    # print(url)

    # Execute request and get response as JSON
    response = requests.get(url, headers={"x-api-key": API_KEY})
    # print(response)

    if (response.status_code == 200):
        json = response.json()
        # print(json)

        if json["error"] == False:
            # URL to use for file upload
            uploadUrl = json["presignedUrl"]
            # # URL for future reference
            uploadedFileUrl = json["url"]

            with open(fileName, 'rb') as file:
                requests.put(uploadUrl, data=file, headers={"x-api-key":API_KEY,  "content-type": "application/json"})

            return uploadedFileUrl
        else:
            # Show service reported error
            print(json["message"])
    else:
        print(f"Request error: {response.status_code} {response.reason}")

    return None


if __name__ == '__main__':
    main()