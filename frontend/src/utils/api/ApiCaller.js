import axios from "axios";

export async function callApi({
  url,
  method = "GET",
  payload = null,
  headers = {},
  retry = 3,
  delay = 5000,
}) {
  try {
    const config = {
      method,
      url,
      headers,
      data: payload,
      withCredentials: true,
    };
    const response = await axios(config);

    return response.data;
  } catch (error) {
    console.error("API call failed:", error);
    throw error.response?.data || error.message;
  }
}
