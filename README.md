# Cara pakai API

## Enpoint 1
`
endpoint : (baseurl)/services/{episode}
method: get
contoh request : http://192.168.38.111:2000//services/one
contoh response : 
    response : {
        "status": 200,
        "message status": "success",
        "data": {
          "Movie": "Peaky Blinders",
          "No.overall": "1",
          "No. inseries": "1",
          "Episode": "Episode 1",
          "Directed by": "tomy",
          "Written by": "tomy",
          "Original air date": "12 September 2013",
          "UK viewers(millions) [2]": "3.05"
        }
      }
      `

## Endpoint 2
`
endpoint 2: (baseurl)/services/{id}
method: post
request body: 
    {
      "directed_by": "string",
      "written_by": "string"
    }

========= Penggunaan =========
contoh request : http://192.168.38.111:2000//services/1
request body: 
    {
      "directed_by": "Jokowi",
      "written_by": "Jokowi"
    }
contoh response : 
    {
      "Movie": "Peaky Blinders",
      "No.overall": "1",
      "No. inseries": "1",
      "Episode": "Episode 1",
      "Directed by": "Jokowi",
      "Written by": "Jokowi",
      "Original air date": "12 September 2013",
      "UK viewers(millions) [2]": "3.05"
    }`
