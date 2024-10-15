import asyncio
import json  # To handle saving JSON data
from playwright.async_api import async_playwright

async def get_land_id_details(email, password, lat, lng):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        # Step 1: Go to Land.id and perform login
        await page.goto("https://id.land/users/sign_in")
        await page.fill('input[name="email"]', email)
        await page.fill('input[name="password"]', password)
        await page.click('button[type="submit"]')

        # Step 2: Capture the network request containing the auth token and email
        auth_data = {"auth_token": None, "auth_email": None}

        async def capture_response(response):
            if "sign_in.json" in response.url:
                print(f"Captured response from {response.url}")  # Log the URL for debugging
                try:
                    json_data = await response.json()
                    # print(f"Full response JSON: {json_data}")  # Print full JSON for debugging

                    # Access the token and email from the nested 'resource' key
                    resource = json_data.get("resource", {})
                    auth_data["auth_token"] = resource.get("authentication_token")
                    auth_data["auth_email"] = resource.get("email")
                    
                    # print(f"Auth Token: {auth_data['auth_token']}")
                    # print(f"Auth Email: {auth_data['auth_email']}")
                except Exception as e:
                    print(f"Failed to parse JSON response: {e}")

        page.on("response", capture_response)

        # Step 3: Wait for the sign_in.json response to be captured
        await page.wait_for_timeout(5000)  # Wait for 5 seconds to ensure response capture

        if auth_data["auth_token"] is None or auth_data["auth_email"] is None:
            print("Failed to capture authentication details.")
            await browser.close()
            return

        # Step 4: Now use the token to request property details
        print("Making API request to fetch parcel details...")
        parcel_api_url = f"https://parcels.id.land/parcels/v2/by_location.json?lng={lng}&lat={lat}"

        headers = {
            "X-Auth-Token": auth_data["auth_token"],
            "X-Auth-Email": auth_data["auth_email"]
        }

        response = await page.request.get(parcel_api_url, headers=headers)
        parcel_details = await response.json()
        # print(f"Parcel Details: {parcel_details}")

        # Step 5: Save the parcel details to a file
        file_path = "parcel_details.json"
        with open(file_path, 'w') as file:
            json.dump(parcel_details, file, indent=4)  # Save the JSON response with indentation
        print(f"Parcel details saved to {file_path}")

        await browser.close()


# Collect user input from the console
print("Enter your login details(Make sure you have an account on Land.id):")
email = input("Enter your email: ")
password = input("Enter your password: ")
latitude = input("Enter the latitude: ")
longitude = input("Enter the longitude: ")

# Convert latitude and longitude to float since they are numerical values
latitude = float(latitude)
longitude = float(longitude)

asyncio.run(get_land_id_details(email, password, latitude, longitude))
