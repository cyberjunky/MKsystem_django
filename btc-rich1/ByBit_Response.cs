using Newtonsoft.Json;

namespace btc_rich1
{
    public class ByBit_Response
    {
        [JsonProperty("ret_code")]
        public int RetCode;
        [JsonProperty("ret_msg")]
        public string RetMsg;
        [JsonProperty("ext_code")]
        public string ExtCode;
        [JsonProperty("ext_info")]
        public string ExtInfo;
        [JsonProperty("result")]
        public object Result;
        [JsonProperty("time_now")]
        public string TimeNow;
    }
}
