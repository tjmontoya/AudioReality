from flask import Flask ,request,jsonify
import requests
import config
import replicate
import re
import openai
import io

# Use pharmapsychotic's clip interrogator model.
model = replicate.models.get("pharmapsychotic/clip-interrogator")
version = model.versions.get("a4a8bafd6089e1716b06057c42b19378250d008b80fe87caa5cd36d40c1eda90")

app = Flask(__name__)

def image_scraper(latitude, longitude):
    URL = "https://maps.googleapis.com/maps/api/streetview?size=600x300&location=" + latitude + "," + longitude + "&heading=151.78&pitch=-0.76&key=" + config.streetview_api_key 
    # URL = "https://maps.googleapis.com/maps/api/streetview?size=600x300&location=4000.414382,10.013988&heading=151.78&pitch=-0.76&key=AIzaSyBIvRdrpXd-Yi86P-dyaDlZwcneBmhzIkY"
    getURL = requests.get(URL)
    if (getURL.status_code == 200):
        # fp = open('image_to_describe.jpg', 'wb')
        # fp.write(getURL.content)
        inputs = {
        # Input image
        'image': io.BytesIO(getURL.content),
        #rb means read binary

        # Choose ViT-L for Stable Diffusion 1, and ViT-H for Stable Diffusion
        # 2
        'clip_model_name': "ViT-L-14/openai",

        # Prompt mode (best takes 10-20 seconds, fast takes 1-2 seconds).
        'mode': "fast",
        }
    output = version.predict(**inputs)
    if ("computer" in output) and ("broken" in output) and ("message" in output):
        ci_analyzed_text = "Location is not available"
    else:
        output = output.replace(',', '')
        output = re.sub('[0-9]', '', output)

        stopwords = ['google', 'image', 'street', 'view', 'maps', '360', 
                'degree', 'º', '360º', '(', ')']
        querywords = output.split(' ')
        resultwords = []
        for i in range(len(querywords)):
            if querywords[i] not in stopwords:
                resultwords.append(querywords[i])
            output = ' '.join(resultwords)

        ci_analyzed_text = ' '.join(output.split())

    user_input = ci_analyzed_text

    def gpt_generate():
        openai.api_key = config.gpt_api_key

        def generate_response(prompt):
            completions = openai.Completion.create(
                engine="text-davinci-002",
                # engine = "GPT-3",
                prompt=prompt,
                max_tokens=2000,
                n=1,
                stop=None,
                temperature=0.3,
            )

            message = completions.choices[0].text
            # print(message)
            return message

    # if image_analyzer.stop_program == True:
    #     # print("Error reading processed image. File accessing error.")
    #     return("Error reading processed image. File accessing error.")
        if user_input == "Location is not available":
            # print(user_input)
            return(user_input)
        else:
            final_input = "Given the following prompt, describe it to a blind person poetically as if he is watching the scene around him and do not infer: " + user_input
            response = generate_response(final_input)
            response = response.replace('\n', '')
            # print(f"{response}")
            return(f"{response}") 

    return gpt_generate()  
        

@app.route('/')
def home():
    return 'Home Page Route'


@app.route('/api',methods=['GET'])
def get_query():
    d ={}
    long_lat_comb = str(request.args['Query'])
    long_lat_split = long_lat_comb.split("/", 1)
    latitude = long_lat_split[0]
    longitude = long_lat_split[1]
    d["description"] = image_scraper(latitude, longitude)
    # print(d["description"])
    return jsonify(d)


if __name__ == '__main__':
	app.run()