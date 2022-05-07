import codecs
import json
import os
import pathlib


if __name__ == "__main__":
    json_path = pathlib.Path(__file__).parent.parent
    print('Path: ', json_path)
    json_files = ("svoboda_articles.json", "lentaru_articles.json")
    json_data = []
    try:
        os.rmdir(str(json_path / "sas_ready_txt"))
    except FileNotFoundError:
        pass
    os.mkdir(str(json_path / "sas_ready_txt"))

    for json_file in json_files:
        with open(str(json_path / json_file)) as json_fileopen:
            json_data = json.load(json_fileopen)
        for article in json_data:
            article_text = ""
            if len(article['article_title']) > 0:
                article_text = (
                    article['article_title'][0]
                    .replace("\n", "") + "\n\n" + article['article_text']
                    .replace("\xa0", " ")
                )
            else:
                article_text = ""
            article_uuid = article['article_uuid']
            filename = article_uuid + ".txt"
            with codecs.open(
                str(json_path / "sas_ready_txt" / filename),
                "w",
                "utf-8-sig",
            ) as temp:
                temp.write(article_text)
