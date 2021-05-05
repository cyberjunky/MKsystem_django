using Newtonsoft.Json;
using System;

namespace btc_rich1
{
    public class ByBit_OrderBookData
    {
        [JsonProperty("symbol")]
        public string Symbol;
        [JsonProperty("price")]
        public Decimal Price;
        [JsonProperty("size")]
        public Decimal Size;
        [JsonProperty("side")]
        public string Side;
    }
}
