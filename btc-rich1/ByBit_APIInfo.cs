using Newtonsoft.Json;

namespace btc_rich1
{
    public class ByBit_APIInfo
    {
        [JsonProperty("api_key")]
        public string ApiKey;
        [JsonProperty("type")]
        public string Type;
        [JsonProperty("user_id")]
        public long UserID;
    }
}
