# Copilot CLI Session

> [!NOTE]
> - **Session ID:** `6e0bd171-e91d-44b0-bdee-28d9c9b5bb09`  
> - **Started:** 7/23/2026, 12:42:21 PM  
> - **Duration:** 10m 38s  
> - **Exported:** 7/23/2026, 12:53:00 PM  

---

<sub>0s</sub>

### Info

Tip: /resume

---

<sub>0s</sub>

### Info

No copilot-instructions.md found. Run /init to generate.

---

<sub>40s</sub>

### User

added some instructions to linear regression notebook to create a scatter plot in the notebook, see what you can do

---

<sub>44s</sub>

### Copilot

I’ll locate the linear regression notebook and wire in the scatter-plot instructions directly in the notebook cells.

---

<sub>46s</sub>

### `glob`

****/*linear*regression*.ipynb**

"**/*linear*regression*.ipynb"

```
No files matched the pattern.
```


---

<sub>47s</sub>

### `rg`

**scatter|Scatter|linear regression|Linear Regression**

"scatter|Scatter|linear regression|Linear Regression" in **/*.ipynb

<details>
<summary>7 matches</summary>

```
.\.ipynb_checkpoints\k-Means-checkpoint.ipynb:239:    "plt.scatter(X['total_bill'], X['size'], c=model_predict, cmap='rainbow', s=50)\n",
.\.ipynb_checkpoints\k-Means-checkpoint.ipynb:240:    "plt.scatter(centroids[:, 0], centroids[:, 1], c='black', s=200, alpha=1)"
.\k-Means.ipynb:347:    "plt.scatter(X['total_bill'], X['size'], c=model_predict, cmap='rainbow', s=50)\n",
.\k-Means.ipynb:348:    "plt.scatter(centroids[:, 0], centroids[:, 1], c='black', s=200, alpha=1)"
.\Linear Regression.ipynb:65:    "* simple scatter plot below"
.\Linear Regression.ipynb:1731:       "            positive: bool, default=False<br><br>When set to ``True``, forces the coefficients to be positive. This<br>option is only supported for dense arrays.<br><br>For a comparison between a linear regression model with positive constraints<br>on the regression coefficients and a linear regression without such constraints,<br>see :ref:`sphx_glr_auto_examples_linear_model_plot_nnls.py`.<br><br>.. versionadded:: 0.24</span>\n",
.\Linear Regression.ipynb:1761:       "            coef_: array of shape (n_features, ) or (n_targets, n_features)<br><br>Estimated coefficients for the linear regression problem.<br>If multiple targets are passed during the fit (y 2D), this<br>is a 2D array of shape (n_targets, n_features), while if only<br>one target is passed, this is a 1D array of length n_features.</span>\n",
```

</details>


---

<sub>51s</sub>

### `view`

**view the file at C:\Users\t-ste\Documents\GitHub\2026-fall\machine-learning\ml-for-absolute-beginners\Linear Regression.ipynb.**

C:\Users\t-ste\Documents\GitHub\2026-fall\machine-learning\ml-for-absolute-beginners\Linear Regression.ipynb (lines 1-180)

<details>
<summary>180 lines</summary>

```
1. {
2.  "cells": [
3.   {
4.    "cell_type": "markdown",
5.    "id": "47ba215d-03c5-4448-9869-602c0d0446a4",
6.    "metadata": {
7.     "canvas": {
8.      "comments": [],
9.      "componentType": "CodeCell",
10.      "copiedOriginId": null,
11.      "diskcache": false,
12.      "headerColor": "none",
13.      "id": "7d4608f8-8d37-47d3-b05a-20fd8f821198",
14.      "isComponent": false,
15.      "name": "",
16.      "parents": []
17.     },
18.     "jp-MarkdownHeadingCollapsed": true,
19.     "tags": []
20.    },
21.    "source": [
22.     "# Import the libraries"
23.    ]
24.   },
25.   {
26.    "cell_type": "code",
27.    "execution_count": 18,
28.    "id": "18198307-f79d-478d-bad0-681a65c064a5",
29.    "metadata": {
30.     "canvas": {
31.      "comments": [],
32.      "componentType": "CodeCell",
33.      "copiedOriginId": null,
34.      "diskcache": false,
35.      "headerColor": "none",
36.      "id": "dd4546a4-b86a-4ea7-80a2-f9251981aec2",
37.      "isComponent": false,
38.      "name": "",
39.      "parents": []
40.     }
41.    },
42.    "outputs": [],
43.    "source": [
44.     "import pandas as pd\n",
45.     "from sklearn.model_selection import train_test_split\n",
46.     "from sklearn.linear_model import LinearRegression\n",
47.     "from sklearn.metrics import mean_absolute_error\n",
48.     "import seaborn as sns\n",
49.     "import matplotlib.pyplot as plt\n",
50.     "\n",
51.     "%matplotlib inline"
52.    ]
53.   },
54.   {
55.    "cell_type": "markdown",
56.    "id": "675b7207",
57.    "metadata": {},
58.    "source": [
59.     "# Seinfeld dataset\n",
60.     "\n",
61.     "ghcp-instructions\n",
62.     "\n",
63.     "* use data/seinfeld.csv\n",
64.     "\n",
65.     "* simple scatter plot below"
66.    ]
67.   },
68.   {
69.    "cell_type": "markdown",
70.    "id": "07b2082f-066f-43de-9716-06206ac2f191",
71.    "metadata": {
72.     "canvas": {
73.      "comments": [],
74.      "componentType": "CodeCell",
75.      "copiedOriginId": null,
76.      "diskcache": false,
77.      "headerColor": "none",
78.      "id": "0d33e4cd-b725-47db-9300-3c29f2c906ef",
79.      "isComponent": false,
80.      "name": "",
81.      "parents": []
82.     },
83.     "jp-MarkdownHeadingCollapsed": true,
84.     "tags": []
85.    },
86.    "source": [
87.     "# Import dataset"
88.    ]
89.   },
90.   {
91.    "cell_type": "code",
92.    "execution_count": 19,
93.    "id": "083b2dd2-3351-44d4-a9ad-41af078b3fcc",
94.    "metadata": {
95.     "canvas": {
96.      "comments": [],
97.      "componentType": "CodeCell",
98.      "copiedOriginId": null,
99.      "diskcache": false,
100.      "headerColor": "none",
101.      "id": "f3e737a2-789a-483b-87fd-f342fb441267",
102.      "isComponent": false,
103.      "name": "",
104.      "parents": []
105.     }
106.    },
107.    "outputs": [
108.     {
109.      "data": {
110.       "text/html": [
111.        "<div>\n",
112.        "<style scoped>\n",
113.        "    .dataframe tbody tr th:only-of-type {\n",
114.        "        vertical-align: middle;\n",
115.        "    }\n",
116.        "\n",
117.        "    .dataframe tbody tr th {\n",
118.        "        vertical-align: top;\n",
119.        "    }\n",
120.        "\n",
121.        "    .dataframe thead th {\n",
122.        "        text-align: right;\n",
123.        "    }\n",
124.        "</style>\n",
125.        "<table border=\"1\" class=\"dataframe\">\n",
126.        "  <thead>\n",
127.        "    <tr style=\"text-align: right;\">\n",
128.        "      <th></th>\n",
129.        "      <th>total_bill</th>\n",
130.        "      <th>tip</th>\n",
131.        "      <th>sex</th>\n",
132.        "      <th>smoker</th>\n",
133.        "      <th>day</th>\n",
134.        "      <th>time</th>\n",
135.        "      <th>size</th>\n",
136.        "    </tr>\n",
137.        "  </thead>\n",
138.        "  <tbody>\n",
139.        "    <tr>\n",
140.        "      <th>0</th>\n",
141.        "      <td>16.99</td>\n",
142.        "      <td>1.01</td>\n",
143.        "      <td>Female</td>\n",
144.        "      <td>No</td>\n",
145.        "      <td>Sun</td>\n",
146.        "      <td>Dinner</td>\n",
147.        "      <td>2</td>\n",
148.        "    </tr>\n",
149.        "    <tr>\n",
150.        "      <th>1</th>\n",
151.        "      <td>10.34</td>\n",
152.        "      <td>1.66</td>\n",
153.        "      <td>Male</td>\n",
154.        "      <td>No</td>\n",
155.        "      <td>Sun</td>\n",
156.        "      <td>Dinner</td>\n",
157.        "      <td>3</td>\n",
158.        "    </tr>\n",
159.        "    <tr>\n",
160.        "      <th>2</th>\n",
161.        "      <td>21.01</td>\n",
162.        "      <td>3.50</td>\n",
163.        "      <td>Male</td>\n",
164.        "      <td>No</td>\n",
165.        "      <td>Sun</td>\n",
166.        "      <td>Dinner</td>\n",
167.        "      <td>3</td>\n",
168.        "    </tr>\n",
169.        "    <tr>\n",
170.        "      <th>3</th>\n",
171.        "      <td>23.68</td>\n",
172.        "      <td>3.31</td>\n",
173.        "      <td>Male</td>\n",
174.        "      <td>No</td>\n",
175.        "      <td>Sun</td>\n",
176.        "      <td>Dinner</td>\n",
177.        "      <td>2</td>\n",
178.        "    </tr>\n",
179.        "    <tr>\n",
180.        "      <th>4</th>\n",
```

</details>


---

<sub>52s</sub>

### `rg`

**TODO|simple scatter plot below|plt\.|scatter\(|sns\.**

"TODO|simple scatter plot below|plt\.|scatter\(|sns\." (Linear Regression.ipynb)

```
C:\Users\t-ste\Documents\GitHub\2026-fall\machine-learning\ml-for-absolute-beginners\Linear Regression.ipynb:65:    "* simple scatter plot below"
C:\Users\t-ste\Documents\GitHub\2026-fall\machine-learning\ml-for-absolute-beginners\Linear Regression.ipynb:296:    "sns.heatmap(df_corr, annot=True, cmap='coolwarm')"
C:\Users\t-ste\Documents\GitHub\2026-fall\machine-learning\ml-for-absolute-beginners\Linear Regression.ipynb:339:    "sns.pairplot(df)"
```


---

<sub>58s</sub>

### `view`

**view the file at C:\Users\t-ste\Documents\GitHub\2026-fall\machine-learning\ml-for-absolute-beginners\Linear Regression.ipynb.**

C:\Users\t-ste\Documents\GitHub\2026-fall\machine-learning\ml-for-absolute-beginners\Linear Regression.ipynb (lines 240-380)

<details>
<summary>48 lines</summary>

```
240.      "comments": [],
241.      "componentType": "CodeCell",
242.      "copiedOriginId": null,
243.      "diskcache": false,
244.      "headerColor": "none",
245.      "id": "be4128bc-1b9e-4578-bbf1-6bd2215f6b01",
246.      "isComponent": false,
247.      "name": "",
248.      "parents": []
249.     }
250.    },
251.    "outputs": [],
252.    "source": [
253.     "df_corr = df.corr(numeric_only=True)"
254.    ]
255.   },
256.   {
257.    "cell_type": "code",
258.    "execution_count": 21,
259.    "id": "118edfd1-a035-43e3-b73b-84ea327fc027",
260.    "metadata": {
261.     "canvas": {
262.      "comments": [],
263.      "componentType": "CodeCell",
264.      "copiedOriginId": null,
265.      "diskcache": false,
266.      "headerColor": "none",
267.      "id": "8e1275f2-1d0c-4bad-b2e9-e42a4bbe517a",
268.      "isComponent": false,
269.      "name": "",
270.      "parents": []
271.     }
272.    },
273.    "outputs": [
274.     {
275.      "data": {
276.       "text/plain": [
277.        "<Axes: >"
278.       ]
279.      },
280.      "execution_count": 21,
281.      "metadata": {},
282.      "output_type": "execute_result"
283.     },
284.     {
285.      "data": {
286.       "image/png": "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

[Output truncated. Use view_range=[287, ...] to continue reading. In your next response, you may batch this with other view calls. File has at least 2211 lines.]
```

</details>


---

<sub>59s</sub>

### `rg`

**read_csv|seinfeld|tips|data/|X\s*=|y\s*=|train_test_split**

"read_csv|seinfeld|tips|data/|X\s*=|y\s*=|train_test_split" (Linear Regression.ipynb)

<details>
<summary>11 matches</summary>

```
C:\Users\t-ste\Documents\GitHub\2026-fall\machine-learning\ml-for-absolute-beginners\Linear Regression.ipynb:45:    "from sklearn.model_selection import train_test_split\n",
C:\Users\t-ste\Documents\GitHub\2026-fall\machine-learning\ml-for-absolute-beginners\Linear Regression.ipynb:63:    "* use data/seinfeld.csv\n",
C:\Users\t-ste\Documents\GitHub\2026-fall\machine-learning\ml-for-absolute-beginners\Linear Regression.ipynb:208:    "df = pd.read_csv('data/tips.csv')\n",
C:\Users\t-ste\Documents\GitHub\2026-fall\machine-learning\ml-for-absolute-beginners\Linear Regression.ipynb:253:    "df_corr = df.corr(numeric_only=True)"
C:\Users\t-ste\Documents\GitHub\2026-fall\machine-learning\ml-for-absolute-beginners\Linear Regression.ipynb:871:    "X = df.drop(['tip', 'smoker_Yes', 'smoker_No'], axis=1)\n",
C:\Users\t-ste\Documents\GitHub\2026-fall\machine-learning\ml-for-absolute-beginners\Linear Regression.ipynb:872:    "y = df['tip']"
C:\Users\t-ste\Documents\GitHub\2026-fall\machine-learning\ml-for-absolute-beginners\Linear Regression.ipynb:894:    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, shuffle=True)"
C:\Users\t-ste\Documents\GitHub\2026-fall\machine-learning\ml-for-absolute-beginners\Linear Regression.ipynb:1494:       "/* Fitted state for parameter tooltips */\n",
C:\Users\t-ste\Documents\GitHub\2026-fall\machine-learning\ml-for-absolute-beginners\Linear Regression.ipynb:1944:       "            element.style.display = 'none';\n",
C:\Users\t-ste\Documents\GitHub\2026-fall\machine-learning\ml-for-absolute-beginners\Linear Regression.ipynb:1966:       " * https://github.com/skrub-data/skrub/blob/403466d1d5d4dc76a7ef569b3f8228db59a31dc3/skrub/_reporting/_data/templates/report.js#L789\n",
C:\Users\t-ste\Documents\GitHub\2026-fall\machine-learning\ml-for-absolute-beginners\Linear Regression.ipynb:1970:       "    const body = document.querySelector('body');\n",
```

</details>


---

<sub>1m 4s</sub>

### `view`

**view the file at C:\Users\t-ste\Documents\GitHub\2026-fall\machine-learning\ml-for-absolute-beginners\Linear Regression.ipynb.**

C:\Users\t-ste\Documents\GitHub\2026-fall\machine-learning\ml-for-absolute-beginners\Linear Regression.ipynb (lines 186-230)

<details>
<summary>45 lines</summary>

```
186.        "      <td>Dinner</td>\n",
187.        "      <td>4</td>\n",
188.        "    </tr>\n",
189.        "  </tbody>\n",
190.        "</table>\n",
191.        "</div>"
192.       ],
193.       "text/plain": [
194.        "   total_bill   tip     sex smoker  day    time  size\n",
195.        "0       16.99  1.01  Female     No  Sun  Dinner     2\n",
196.        "1       10.34  1.66    Male     No  Sun  Dinner     3\n",
197.        "2       21.01  3.50    Male     No  Sun  Dinner     3\n",
198.        "3       23.68  3.31    Male     No  Sun  Dinner     2\n",
199.        "4       24.59  3.61  Female     No  Sun  Dinner     4"
200.       ]
201.      },
202.      "execution_count": 19,
203.      "metadata": {},
204.      "output_type": "execute_result"
205.     }
206.    ],
207.    "source": [
208.     "df = pd.read_csv('data/tips.csv')\n",
209.     "df.head()"
210.    ]
211.   },
212.   {
213.    "cell_type": "markdown",
214.    "id": "8c47a1a8-3027-479e-9ee7-e09e030323e4",
215.    "metadata": {
216.     "canvas": {
217.      "comments": [],
218.      "componentType": "CodeCell",
219.      "copiedOriginId": null,
220.      "diskcache": false,
221.      "headerColor": "none",
222.      "id": "48a4f14b-304a-447f-818e-e4e41850527e",
223.      "isComponent": false,
224.      "name": "",
225.      "parents": []
226.     },
227.     "jp-MarkdownHeadingCollapsed": true,
228.     "tags": []
229.    },
230.    "source": [
```

</details>


---

<sub>1m 6s</sub>

### `view`

**view the file at C:\Users\t-ste\Documents\GitHub\2026-fall\machine-learning\ml-for-absolute-beginners\Linear Regression.ipynb.**

C:\Users\t-ste\Documents\GitHub\2026-fall\machine-learning\ml-for-absolute-beginners\Linear Regression.ipynb (lines 230-320)

<details>
<summary>58 lines</summary>

```
230.    "source": [
231.     "# Exploratory data analysis"
232.    ]
233.   },
234.   {
235.    "cell_type": "code",
236.    "execution_count": 20,
237.    "id": "08cd5043-6b42-4699-bbb4-f3edd9311eab",
238.    "metadata": {
239.     "canvas": {
240.      "comments": [],
241.      "componentType": "CodeCell",
242.      "copiedOriginId": null,
243.      "diskcache": false,
244.      "headerColor": "none",
245.      "id": "be4128bc-1b9e-4578-bbf1-6bd2215f6b01",
246.      "isComponent": false,
247.      "name": "",
248.      "parents": []
249.     }
250.    },
251.    "outputs": [],
252.    "source": [
253.     "df_corr = df.corr(numeric_only=True)"
254.    ]
255.   },
256.   {
257.    "cell_type": "code",
258.    "execution_count": 21,
259.    "id": "118edfd1-a035-43e3-b73b-84ea327fc027",
260.    "metadata": {
261.     "canvas": {
262.      "comments": [],
263.      "componentType": "CodeCell",
264.      "copiedOriginId": null,
265.      "diskcache": false,
266.      "headerColor": "none",
267.      "id": "8e1275f2-1d0c-4bad-b2e9-e42a4bbe517a",
268.      "isComponent": false,
269.      "name": "",
270.      "parents": []
271.     }
272.    },
273.    "outputs": [
274.     {
275.      "data": {
276.       "text/plain": [
277.        "<Axes: >"
278.       ]
279.      },
280.      "execution_count": 21,
281.      "metadata": {},
282.      "output_type": "execute_result"
283.     },
284.     {
285.      "data": {
286.       "image/png": "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

[Output truncated. Use view_range=[287, ...] to continue reading. In your next response, you may batch this with other view calls. File has at least 2211 lines.]
```

</details>


---

<sub>1m 10s</sub>

### Copilot

I found the instruction block in `Linear Regression.ipynb`; next I’ll align the dataset and add a simple scatter plot cell there.

---

<sub>1m 12s</sub>

### `powershell`

**Preview Seinfeld CSV columns**

<details>
<summary>Arguments</summary>

```json
{
  "command": "Get-Content -Path 'C:\\Users\\t-ste\\Documents\\GitHub\\2026-fall\\machine-learning\\ml-for-absolute-beginners\\data\\seinfeld.csv' -TotalCount 8",
  "description": "Preview Seinfeld CSV columns"
}
```

</details>

<details>
<summary>9 lines</summary>

```
season,viewers-in-millions
1,19.22
2,18.07
3,17.67
4,20.52
5,29.59
6,31.27
7,33.19
<shellId: 0 completed with exit code 0>
```

</details>


---

<sub>1m 18s</sub>

### `view`

**view the file at C:\Users\t-ste\Documents\GitHub\2026-fall\machine-learning\ml-for-absolute-beginners\Linear Regression.ipynb.**

C:\Users\t-ste\Documents\GitHub\2026-fall\machine-learning\ml-for-absolute-beginners\Linear Regression.ipynb (lines 54-110)

<details>
<summary>57 lines</summary>

```
54.   {
55.    "cell_type": "markdown",
56.    "id": "675b7207",
57.    "metadata": {},
58.    "source": [
59.     "# Seinfeld dataset\n",
60.     "\n",
61.     "ghcp-instructions\n",
62.     "\n",
63.     "* use data/seinfeld.csv\n",
64.     "\n",
65.     "* simple scatter plot below"
66.    ]
67.   },
68.   {
69.    "cell_type": "markdown",
70.    "id": "07b2082f-066f-43de-9716-06206ac2f191",
71.    "metadata": {
72.     "canvas": {
73.      "comments": [],
74.      "componentType": "CodeCell",
75.      "copiedOriginId": null,
76.      "diskcache": false,
77.      "headerColor": "none",
78.      "id": "0d33e4cd-b725-47db-9300-3c29f2c906ef",
79.      "isComponent": false,
80.      "name": "",
81.      "parents": []
82.     },
83.     "jp-MarkdownHeadingCollapsed": true,
84.     "tags": []
85.    },
86.    "source": [
87.     "# Import dataset"
88.    ]
89.   },
90.   {
91.    "cell_type": "code",
92.    "execution_count": 19,
93.    "id": "083b2dd2-3351-44d4-a9ad-41af078b3fcc",
94.    "metadata": {
95.     "canvas": {
96.      "comments": [],
97.      "componentType": "CodeCell",
98.      "copiedOriginId": null,
99.      "diskcache": false,
100.      "headerColor": "none",
101.      "id": "f3e737a2-789a-483b-87fd-f342fb441267",
102.      "isComponent": false,
103.      "name": "",
104.      "parents": []
105.     }
106.    },
107.    "outputs": [
108.     {
109.      "data": {
110.       "text/html": [
```

</details>


---

<sub>1m 47s</sub>

### `apply_patch`

<details>
<summary>Arguments</summary>

```json
"*** Begin Patch\n*** Update File: C:\\Users\\t-ste\\Documents\\GitHub\\2026-fall\\machine-learning\\ml-for-absolute-beginners\\Linear Regression.ipynb\n@@\n   {\n    \"cell_type\": \"markdown\",\n    \"id\": \"675b7207\",\n    \"metadata\": {},\n    \"source\": [\n     \"# Seinfeld dataset\\n\",\n     \"\\n\",\n     \"ghcp-instructions\\n\",\n     \"\\n\",\n     \"* use data/seinfeld.csv\\n\",\n     \"\\n\",\n     \"* simple scatter plot below\"\n    ]\n   },\n+  {\n+   \"cell_type\": \"code\",\n+   \"execution_count\": null,\n+   \"id\": \"seinfeld-scatter\",\n+   \"metadata\": {},\n+   \"outputs\": [],\n+   \"source\": [\n+    \"df_seinfeld = pd.read_csv('data/seinfeld.csv')\\n\",\n+    \"sns.scatterplot(data=df_seinfeld, x='season', y='viewers-in-millions')\\n\",\n+    \"plt.title('Seinfeld viewers by season')\\n\",\n+    \"plt.xlabel('Season')\\n\",\n+    \"plt.ylabel('Viewers (millions)')\\n\",\n+    \"plt.show()\"\n+   ]\n+  },\n   {\n    \"cell_type\": \"markdown\",\n    \"id\": \"07b2082f-066f-43de-9716-06206ac2f191\",\n*** End Patch\n"
```

</details>

```
Modified 1 file(s): C:\Users\t-ste\Documents\GitHub\2026-fall\machine-learning\ml-for-absolute-beginners\Linear Regression.ipynb
```


---

<sub>2m 10s</sub>

### `powershell` — Failed

**Validate notebook JSON**

<details>
<summary>Arguments</summary>

```json
{
  "command": "python -c \"import json, pathlib; p=pathlib.Path(r'C:\\Users\\t-ste\\Documents\\GitHub\\2026-fall\\machine-learning\\ml-for-absolute-beginners\\Linear Regression.ipynb'); json.load(p.open('r', encoding='utf-8')); print('ok')\"",
  "description": "Validate notebook JSON"
}
```

</details>

```
The user rejected this tool call. User feedback: notebook works, just add the new and i will test
```


---

<sub>2m 11s</sub>

### Copilot

Added a new code cell directly under the **Seinfeld dataset** instructions in `Linear Regression.ipynb` that:

- loads `data/seinfeld.csv` into `df_seinfeld`
- creates a simple scatter plot of `season` vs `viewers-in-millions`
- adds title/axis labels and shows the plot

I left the rest of the notebook unchanged so you can run and test this new cell in place.

---

<sub>3m 25s</sub>

### User

y axis 0 to 40

---

<sub>3m 28s</sub>

### Copilot

I’ll update the scatter plot cell to fix the y-axis range to 0–40.

---

<sub>3m 31s</sub>

### `apply_patch`

<details>
<summary>Arguments</summary>

```json
"*** Begin Patch\n*** Update File: C:\\Users\\t-ste\\Documents\\GitHub\\2026-fall\\machine-learning\\ml-for-absolute-beginners\\Linear Regression.ipynb\n@@\n     \"sns.scatterplot(data=df_seinfeld, x='season', y='viewers-in-millions')\\n\",\n     \"plt.title('Seinfeld viewers by season')\\n\",\n     \"plt.xlabel('Season')\\n\",\n     \"plt.ylabel('Viewers (millions)')\\n\",\n+    \"plt.ylim(0, 40)\\n\",\n     \"plt.show()\"\n    ]\n   },\n*** End Patch\n"
```

</details>

```
Modified 1 file(s): C:\Users\t-ste\Documents\GitHub\2026-fall\machine-learning\ml-for-absolute-beginners\Linear Regression.ipynb
```


---

<sub>3m 34s</sub>

### Copilot

Done — the Seinfeld scatter plot cell now sets the y-axis to **0 through 40** with:

```python
plt.ylim(0, 40)
```

---

<sub>4m 6s</sub>

### User

add linear regression line

---

<sub>4m 13s</sub>

### Copilot

I’ll add a fitted regression line on top of the existing scatter plot in that Seinfeld cell.

---

<sub>4m 16s</sub>

### `apply_patch`

<details>
<summary>Arguments</summary>

```json
"*** Begin Patch\n*** Update File: C:\\Users\\t-ste\\Documents\\GitHub\\2026-fall\\machine-learning\\ml-for-absolute-beginners\\Linear Regression.ipynb\n@@\n     \"df_seinfeld = pd.read_csv('data/seinfeld.csv')\\n\",\n     \"sns.scatterplot(data=df_seinfeld, x='season', y='viewers-in-millions')\\n\",\n+    \"sns.regplot(data=df_seinfeld, x='season', y='viewers-in-millions', scatter=False, ci=None, color='red')\\n\",\n     \"plt.title('Seinfeld viewers by season')\\n\",\n*** End Patch\n"
```

</details>

```
Modified 1 file(s): C:\Users\t-ste\Documents\GitHub\2026-fall\machine-learning\ml-for-absolute-beginners\Linear Regression.ipynb
```


---

<sub>4m 17s</sub>

### Copilot

Added a linear regression line to the Seinfeld plot cell by overlaying:

```python
sns.regplot(data=df_seinfeld, x='season', y='viewers-in-millions', scatter=False, ci=None, color='red')
```

So it now shows the scatter points plus a red best-fit line.

---

<sub>5m 5s</sub>

### User

magenta line

---

<sub>5m 9s</sub>

### `apply_patch`

<details>
<summary>Arguments</summary>

```json
"*** Begin Patch\n*** Update File: C:\\Users\\t-ste\\Documents\\GitHub\\2026-fall\\machine-learning\\ml-for-absolute-beginners\\Linear Regression.ipynb\n@@\n-    \"sns.regplot(data=df_seinfeld, x='season', y='viewers-in-millions', scatter=False, ci=None, color='red')\\n\",\n+    \"sns.regplot(data=df_seinfeld, x='season', y='viewers-in-millions', scatter=False, ci=None, color='magenta')\\n\",\n*** End Patch\n"
```

</details>

```
Modified 1 file(s): C:\Users\t-ste\Documents\GitHub\2026-fall\machine-learning\ml-for-absolute-beginners\Linear Regression.ipynb
```


---

<sub>5m 10s</sub>

### Copilot

Done — the regression line is now **magenta**.

---

<sub>6m 29s</sub>

### User

plot difference lines between point and regression line, thin blue

---

<sub>6m 34s</sub>

### Copilot

I’ll update the Seinfeld plot cell to draw thin blue residual lines from each point to the regression line.

---

<sub>6m 36s</sub>

### `rg`

**df_seinfeld = pd.read_csv\('data/seinfeld.csv'\)|sns\.regplot\(data=df_seinfeld**

"df_seinfeld = pd.read_csv\('data/seinfeld.csv'\)|sns\.regplot\(data=df_seinfeld" (Linear Regression.ipynb)

```
C:\Users\t-ste\Documents\GitHub\2026-fall\machine-learning\ml-for-absolute-beginners\Linear Regression.ipynb:86:    "df_seinfeld = pd.read_csv('data/seinfeld.csv')\n",
C:\Users\t-ste\Documents\GitHub\2026-fall\machine-learning\ml-for-absolute-beginners\Linear Regression.ipynb:88:    "sns.regplot(data=df_seinfeld, x='season', y='viewers-in-millions', scatter=False, ci=None, color='magenta')\n",
```


---

<sub>6m 41s</sub>

### `apply_patch`

<details>
<summary>Arguments</summary>

```json
"*** Begin Patch\n*** Update File: C:\\Users\\t-ste\\Documents\\GitHub\\2026-fall\\machine-learning\\ml-for-absolute-beginners\\Linear Regression.ipynb\n@@\n     \"df_seinfeld = pd.read_csv('data/seinfeld.csv')\\n\",\n+    \"X_seinfeld = df_seinfeld[['season']]\\n\",\n+    \"y_seinfeld = df_seinfeld['viewers-in-millions']\\n\",\n+    \"seinfeld_model = LinearRegression()\\n\",\n+    \"seinfeld_model.fit(X_seinfeld, y_seinfeld)\\n\",\n+    \"y_seinfeld_pred = seinfeld_model.predict(X_seinfeld)\\n\",\n     \"sns.scatterplot(data=df_seinfeld, x='season', y='viewers-in-millions')\\n\",\n     \"sns.regplot(data=df_seinfeld, x='season', y='viewers-in-millions', scatter=False, ci=None, color='magenta')\\n\",\n+    \"for season, actual, predicted in zip(df_seinfeld['season'], y_seinfeld, y_seinfeld_pred):\\n\",\n+    \"    plt.plot([season, season], [actual, predicted], color='blue', linewidth=0.8)\\n\",\n     \"plt.title('Seinfeld viewers by season')\\n\",\n*** End Patch\n"
```

</details>

```
Modified 1 file(s): C:\Users\t-ste\Documents\GitHub\2026-fall\machine-learning\ml-for-absolute-beginners\Linear Regression.ipynb
```


---

<sub>6m 44s</sub>

### Copilot

Done — I added **thin blue residual lines** from each point to the fitted regression line in the Seinfeld plot cell (`linewidth=0.8`, `color='blue'`).

---

<sub>7m 25s</sub>

### User

project forward for season 10

---

<sub>7m 27s</sub>

### Copilot

I’ll extend the same Seinfeld plot cell to predict and display the season 10 projection from the fitted model.

---

<sub>7m 30s</sub>

### `view`

**view the file at C:\Users\t-ste\Documents\GitHub\2026-fall\machine-learning\ml-for-absolute-beginners\Linear Regression.ipynb.**

C:\Users\t-ste\Documents\GitHub\2026-fall\machine-learning\ml-for-absolute-beginners\Linear Regression.ipynb (lines 78-120)

<details>
<summary>43 lines</summary>

```
78.        "<Figure size 640x480 with 1 Axes>"
79.       ]
80.      },
81.      "metadata": {},
82.      "output_type": "display_data"
83.     }
84.    ],
85.    "source": [
86.     "df_seinfeld = pd.read_csv('data/seinfeld.csv')\n",
87.     "X_seinfeld = df_seinfeld[['season']]\n",
88.     "y_seinfeld = df_seinfeld['viewers-in-millions']\n",
89.     "seinfeld_model = LinearRegression()\n",
90.     "seinfeld_model.fit(X_seinfeld, y_seinfeld)\n",
91.     "y_seinfeld_pred = seinfeld_model.predict(X_seinfeld)\n",
92.     "sns.scatterplot(data=df_seinfeld, x='season', y='viewers-in-millions')\n",
93.     "sns.regplot(data=df_seinfeld, x='season', y='viewers-in-millions', scatter=False, ci=None, color='magenta')\n",
94.     "for season, actual, predicted in zip(df_seinfeld['season'], y_seinfeld, y_seinfeld_pred):\n",
95.     "    plt.plot([season, season], [actual, predicted], color='blue', linewidth=0.8)\n",
96.     "plt.title('Seinfeld viewers by season')\n",
97.     "plt.xlabel('Season')\n",
98.     "plt.ylabel('Viewers (millions)')\n",
99.     "plt.ylim(0, 40)\n",
100.     "plt.show()"
101.    ]
102.   },
103.   {
104.    "cell_type": "markdown",
105.    "id": "07b2082f-066f-43de-9716-06206ac2f191",
106.    "metadata": {
107.     "canvas": {
108.      "comments": [],
109.      "componentType": "CodeCell",
110.      "copiedOriginId": null,
111.      "diskcache": false,
112.      "headerColor": "none",
113.      "id": "0d33e4cd-b725-47db-9300-3c29f2c906ef",
114.      "isComponent": false,
115.      "name": "",
116.      "parents": []
117.     },
118.     "jp-MarkdownHeadingCollapsed": true,
119.     "tags": []
120.    },
```

</details>


---

<sub>7m 40s</sub>

### `apply_patch`

<details>
<summary>Arguments</summary>

```json
"*** Begin Patch\n*** Update File: C:\\Users\\t-ste\\Documents\\GitHub\\2026-fall\\machine-learning\\ml-for-absolute-beginners\\Linear Regression.ipynb\n@@\n     \"y_seinfeld = df_seinfeld['viewers-in-millions']\\n\",\n     \"seinfeld_model = LinearRegression()\\n\",\n     \"seinfeld_model.fit(X_seinfeld, y_seinfeld)\\n\",\n     \"y_seinfeld_pred = seinfeld_model.predict(X_seinfeld)\\n\",\n+    \"projection_df = pd.DataFrame({'season': range(int(df_seinfeld['season'].min()), 11)})\\n\",\n+    \"projection_pred = seinfeld_model.predict(projection_df[['season']])\\n\",\n+    \"season_10_pred = seinfeld_model.predict(pd.DataFrame({'season': [10]}))[0]\\n\",\n     \"sns.scatterplot(data=df_seinfeld, x='season', y='viewers-in-millions')\\n\",\n-    \"sns.regplot(data=df_seinfeld, x='season', y='viewers-in-millions', scatter=False, ci=None, color='magenta')\\n\",\n+    \"plt.plot(projection_df['season'], projection_pred, color='magenta')\\n\",\n+    \"plt.scatter([10], [season_10_pred], color='magenta', s=60)\\n\",\n     \"for season, actual, predicted in zip(df_seinfeld['season'], y_seinfeld, y_seinfeld_pred):\\n\",\n     \"    plt.plot([season, season], [actual, predicted], color='blue', linewidth=0.8)\\n\",\n     \"plt.title('Seinfeld viewers by season')\\n\",\n     \"plt.xlabel('Season')\\n\",\n     \"plt.ylabel('Viewers (millions)')\\n\",\n+    \"plt.xlim(df_seinfeld['season'].min() - 0.5, 10.5)\\n\",\n     \"plt.ylim(0, 40)\\n\",\n+    \"print(f'Season 10 projected viewers (millions): {season_10_pred:.2f}')\\n\",\n     \"plt.show()\"\n    ]\n   },\n*** End Patch\n"
```

</details>

```
Modified 1 file(s): C:\Users\t-ste\Documents\GitHub\2026-fall\machine-learning\ml-for-absolute-beginners\Linear Regression.ipynb
```


---

<sub>7m 41s</sub>

### Copilot

Done — I updated the Seinfeld plot cell to **project forward to season 10** using the fitted linear model.

It now:
- extends the magenta regression line through season 10,
- plots the season 10 projected point in magenta,
- prints the projected season 10 viewers value.

---

<sub>9m 11s</sub>

### User

maybe y axis to 45 and horizontal and vertical grid lines every 10 on y axis and each season on x axis

---

<sub>9m 18s</sub>

### `apply_patch`

<details>
<summary>Arguments</summary>

```json
"*** Begin Patch\n*** Update File: C:\\Users\\t-ste\\Documents\\GitHub\\2026-fall\\machine-learning\\ml-for-absolute-beginners\\Linear Regression.ipynb\n@@\n     \"plt.title('Seinfeld viewers by season')\\n\",\n     \"plt.xlabel('Season')\\n\",\n     \"plt.ylabel('Viewers (millions)')\\n\",\n     \"plt.xlim(df_seinfeld['season'].min() - 0.5, 10.5)\\n\",\n-    \"plt.ylim(0, 40)\\n\",\n+    \"plt.ylim(0, 45)\\n\",\n+    \"plt.xticks(range(int(df_seinfeld['season'].min()), 11, 1))\\n\",\n+    \"plt.yticks(range(0, 46, 10))\\n\",\n+    \"plt.grid(True, axis='both', which='major', linewidth=0.6, alpha=0.6)\\n\",\n     \"print(f'Season 10 projected viewers (millions): {season_10_pred:.2f}')\\n\",\n     \"plt.show()\"\n    ]\n   },\n*** End Patch\n"
```

</details>

```
Modified 1 file(s): C:\Users\t-ste\Documents\GitHub\2026-fall\machine-learning\ml-for-absolute-beginners\Linear Regression.ipynb
```


---

<sub>9m 19s</sub>

### Copilot

Updated.

The chart now uses:
- **y-axis 0 to 45**
- **horizontal grid lines every 10** on y (`0, 10, 20, 30, 40`)
- **vertical grid lines at each season** on x (each integer season tick through 10)

---

<sub>Generated by [GitHub Copilot CLI](https://github.com/features/copilot/cli)</sub>
