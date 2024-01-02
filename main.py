import pandas as pd
import requests
from bs4 import BeautifulSoup


def main():
    data = {'title': [],
            'name': [],
            'good': [],
            'bad': [],
            'badge': [],
            'lancers_choice': [],
            'price': [],
            'image': []}

    root = 'https://www.lancers.jp'

    # URLを指定
    for page in [1,2]:
        url = f'https://www.lancers.jp/menu/search?identification=0&keyword=%E3%82%B3%E3%83%B3%E3%82%B5%E3%83%AB&primary=45&sort_by=relevant&page={page}'

        # URLからHTMLデータを取得
        response = requests.get(url)
        html = response.text

        # BeautifulSoupでHTMLを解析
        soup = BeautifulSoup(html, 'html.parser')

        # 特定のクラスの要素を抽出
        target_class = 'c-package js-store'
        elements = soup.find_all(class_=target_class)

        soup.find('dd', class_='クラス名').text


        # 抽出された要素を表示
        for element in elements:
            # プロフィールのURLを取得
            profile =
            profele_url = root + profile
            profile_response = requests.get(profile_url)

            title = element.find('a', class_='c-package__heading-link').text.strip()
            name = element.find('a', class_='c-package__avatar-link').text.strip()
            good = element.find('div', class_='c-tooltip c-tooltip--align-left').text.strip().split(' ')[0]
            bad =  element.find('div', class_='c-tooltip u-ml7').text.strip().split(' ')[0]

            if element.find('span', class_='c-badge__text') is not None:
                badge = element.find('span', class_='c-badge__text').text
            else:
                badge = ''

            lancers_choice = (element.find('button', class_='c-package-badges c-tooltip c-tooltip--align-right') is not None)
            price = element.find('div', class_='c-package__price').text.strip()
            if element.find('a', class_='c-package__figure').find('img') is not None:
                img = element.find('a', class_='c-package__figure').find('img').get('src')
            else:
                img = ''

            data['title'].append(title)
            data['name'].append(name)
            data['good'].append(good)
            data['bad'].append(bad)
            data['badge'].append(badge)
            data['lancers_choice'].append(lancers_choice)
            data['price'].append(price)
            data['image'].append(img)

    df = pd.DataFrame(data)
    df.to_csv('lancers.csv')

if __name__ == '__main__':
    main()