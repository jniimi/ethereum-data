# Ethereum Price Change in Russia-Ukraine conflict
This data has been originally collected by [@jniimi_as_jack][twit], a data science researcher in Japan. In this time, he decided to disclose it partly since he prioritizes the public interest.

I hope this data will be utilized in capturing the relationship between the price change of crypto currency and international affairs.

## Citation/Reference when Use
You do not need to contact me to use this data. Instead, regardless of the purpose of use, such as academic use or commercial use, clearly indicate the reference as follows:

### APA
> Junichiro, NIIMI. (2022). Ethereum Price Change in Russia-Ukraine conflict. GitHub Repository. https://github.com/jniimi/ethereum-data.

### BibTeX
```
@misc{ethdata,  
  author = {Junichiro, NIIMI},
  title = {{Ethereum Price Change in Russia-Ukraine conflictMy Research Software}},
  publisher={GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/jniimi/ethereum-data}},
  year = {2022}
}
```

## Background
The data had been collected in followin period, which captures the moment when Ukraine conflict (Russian invasion) obviously began (24 Feb 2022).
- from: 2022-02-23 17:55:54.187000
- to: 2022-02-24 09:09:13.590000

in UTC (based on bitFlyer's server time).

*This is not collected with WebSocket but ordinary GET API with Google Colab so that the data acquisition interval is not strictly every second.

## Data Description
Basically, most of the variables are same as those of bitFlyer's "getticker" in [HTTP Public API][API], containing "product_code", "state", "timestamp", "tick_id", "best_bid", "best_ask", "best_bid_size", "best_ask_size", "total_bid_depth", "total_ask_depth", "market_bid_size", "market_ask_size", "ltp", "volume", and "volume_by_product". 

In addition to them, jniimi added "datetime" which is UTC time converted from "timestamp".

[twit]:https://twitter.com/jniimi_as_jack
[API]:https://lightning.bitflyer.com/docs?lang=en
