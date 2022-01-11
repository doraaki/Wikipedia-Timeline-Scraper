# Wikipedia-Timeline-Scraper
Project to collect a dataset of historic events from Wikipedia.

Wikipedia has pages named `YEAR` in `TOPIC` ([2007 in politics](https://en.wikipedia.org/wiki/2007_in_politics) for example) which contain events that happened in that year.

[MediaWiki](https://www.mediawiki.org/wiki/MediaWiki) provides tools for working with `Wikipedia` knowledge.
The [TextExtracts API](https://www.mediawiki.org/wiki/Extension:TextExtracts) is used to parse pages. If `TextExtracts` doesn't work properly, the page is parsed manually. 
