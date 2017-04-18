from __future__ import absolute_import

from bs4 import BeautifulSoup
import requests


html = requests.get("https://en.wikipedia.org/wiki/IOS_SDK").content

html_parser = BeautifulSoup(html, 'html.parser')
tables = html_parser.select(".wikitable")

# First couple tables are legends, and current releases.
version_tables = tables[2:]

builds = {}

for table in version_tables:
    # Build information listed as
    # <tr><th>version</th>, <td>build number</td>, <td>release date</td>, <td>release notes</td>,
    # <td>itunes version</td>, <td>xcode version</td></tr>

    # First 2 rows are legend information.
    build_history = table.find_all("tr")[2:]
    for row in build_history:
        version = None
        build_number = None
        beta = False
        final = False
        try:
            # Find version, and remove markup.
            version = row.find("th").text.replace("[edit]", "").replace("\n", "")
            if "final" in version.lower():
                final = True

            if "beta" in version.lower():
                beta = True

        except (IndexError, AttributeError):
            # TODO: Cells that are merged throw exceptions
            pass

        try:
            build_number = row.find_all("td")[0].text
        except IndexError:
            # TODO: Merged cells throwing exception.
            pass

        if build_number and version:
            builds[build_number] = {
                "name": version,
                "build": build_number,
                "beta": beta,
                "final": final
            }

print(builds)
