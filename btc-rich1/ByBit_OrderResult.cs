using Newtonsoft.Json;
using System.Collections.Generic;

namespace btc_rich1
{
    public class ByBit_OrderResult
    {
        [JsonProperty("data")]
        public List<ByBit_Order> Data { get; set; }

        [JsonProperty("cursor")]
        public string Cursor { get; set; }
    }
}
