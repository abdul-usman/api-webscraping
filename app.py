def scrape_url(url):
    try:
        # Send an HTTP request to the URL
        response = requests.get(
            url,
            headers={
                'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
            })

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract the content of the first <h1> tag
            h1_tag = soup.find('h1')
            title = h1_tag.text.replace('\n', '').replace(
                'GPL', '') if h1_tag else 'No <h1> tag found'

            # Find the <div> containing the date information
            time = soup.find('span', {'class': 'last-modified-timestamp'})
            time_find = time.text.replace('\n', '') if time else 'not found'

            return {'time': time_find, 'title': title}

        else:
            return {
                'url':
                url,
                'error':
                f'Failed to retrieve the page. Status code: {response.status_code}'
            }

    except Exception as e:
        print(f"Error scraping URL '{url}': {str(e)}")
        return {'url': url, 'error': str(e)}
