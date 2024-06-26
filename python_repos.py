import requests
import plotly.express as px
# Make an API call and check the response.
url = 'https://api.github.com/search/repositories'
url += '?q=language:python+sort:stars+stars:>10000'

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Convert the response object to a dictionary
response_dict = r.json()

print(f"Total repositories: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")

# Explore information about the repositories
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# Examine the first repository
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)

# Process the results
print(response_dict.keys())
# repo_names, stars, hover_texts = [], [], []

repo_links, stars, hover_texts = [], [], []

for repo_dist in repo_dicts:
    # repo_names.append(repo_dict['name'])
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href = '{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])

    # Build hover texts
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

title = 'Most starred Python projects in Github'
labels = {'x': 'Repository','y': 'Stars'}

# Make visualization
# fig = px.bar(x=repo_names, y=stars, title=title, labels = labels, hover_name=hover_texts)
fig = px.bar(x=repo_links, y = stars, title=title, labels = labels, hover_name = hover_texts)
fig.update_layout(title_font_size = 28, xaxis_title_font_size = 20, yaxis_title_font_size = 20)

fig.show()