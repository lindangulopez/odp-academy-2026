---
hide:
  - navigation
  - toc
---

# ODP Academy, Working with Ocean Data on ODP

<div class="story" markdown="1">

<header class="cover bleed">
  <img src="img/south-coast-sea.jpg" alt="Rocky shore and the Indian Ocean on the KwaZulu-Natal South Coast">
  <div class="cover-text">
    <p class="kicker">ODP Academy · November to December 2026</p>
    <h2>Working with Ocean Data, from the coast I grew up on</h2>
    <p class="dek">My progress in HUB Ocean's course on the Ocean Data Platform, and what one question about the Wild Coast seafloor led to.</p>
    <p class="byline">Linda Angulo Lopez · updated 22 November 2026</p>
    <span class="scroll-cue">Scroll to read ↓</span>
  </div>
  <span class="credit">Photo: the Indian Ocean at Margate, KwaZulu-Natal South Coast, by <a href="https://www.flickr.com/photos/65695019@N07/54280264565">Bernard Dupont</a> (CC BY-SA 2.0), via Flickr.</span>
</header>

<div class="read lead" markdown="1">

I am following [*Working with Ocean Data on ODP*](https://www.hubocean.earth/odp-academy-wiomsa-training), a free online course from [HUB Ocean](https://www.hubocean.earth/), [WIOMSA](https://www.wiomsa.org/) (the Western Indian Ocean Marine Science Association) and [SeaSketch](https://www.seasketch.org/). It runs from 12 November to 18 December 2026, 2 to 4 hours a week, with a new module every Thursday. The lessons are on ODP Academy; the data is on the [Ocean Data Platform](https://app.hubocean.earth/) (ODP).

This site shows where I am, module by module. It is a log, so it will change.

</div>

<div class="read" markdown="1">

<span class="section-label">Where I start from</span>

## A botanist from the Wild Coast

I grew up on the Wild Coast in South Africa, on the Indian Ocean, and trained as a botanist. I am a Full Stack GIS Developer, with more than 25 years of work across Europe and Africa in environmental governance, landscape ecology and research infrastructures. Since September 2025 I have been a Partnerships Specialist at Software Heritage. More about me on [my personal site](https://lindangulopez.github.io/personal_knowledge_base/).

QGIS and Python are daily tools for me; ocean data is newer.

</div>

<div class="read" markdown="1">

<span class="section-label">Module 2 exercise</span>

## The Wild Coast seafloor

For a Module 2 lesson I downloaded ODP's global seamount layer, and found no seamount anywhere near the coast I grew up on. So I asked: **what does the Wild Coast's seafloor have instead, and how does it compare with the rest of South Africa's coast?**

</div>

<section class="sidecar" markdown="1">
  <figure class="side-media">
    <img src="img/wild-coast/map_overview.png" alt="South Africa's shelf, canyons and seamounts, with the Wild Coast highlighted">
    <figcaption>South Africa's shelf, canyons and seamounts, with the Wild Coast highlighted. Data: Seafloor Geomorphic Features Map, GRID-Arendal (CC BY 4.0), via ODP.</figcaption>
  </figure>
  <div class="side-text" markdown="1">
<div class="step" markdown="1">

### Four reaches, 302 points

I split South Africa's mainland coast into four reaches (West, South, Wild Coast, KwaZulu-Natal) and placed a point every 10 km along it. At each point I measured the distance to the nearest seamount and the width of the shelf, and I counted the canyons within 100 km of the coast.

</div>
<div class="step" markdown="1">

### Four open layers

The seamounts, canyons, shelf and slope come from the Seafloor Geomorphic Features Map on ODP, read through its OGC API Features with no key. The code is a [notebook](https://github.com/lindangulopez/odp-academy-2026/blob/main/notebooks/wild_coast_seafloor.ipynb); the method and its limits are on the [exercise page](module-2-wild-coast.md).

</div>
  </div>
</section>

<div class="numbers">
  <div class="num"><strong>~190 km</strong><span>to the nearest seamount from the Wild Coast</span></div>
  <div class="num"><strong>14 km</strong><span>median shelf width, against 76 km on the South coast</span></div>
  <div class="num"><strong>3.2</strong><span>canyons per 100 km of coast, the most in South Africa</span></div>
  <div class="num"><strong>6.4 km</strong><span>from shore to the closest canyon, the closest in the country</span></div>
</div>

<section class="sidecar flip" markdown="1">
  <figure class="side-media">
    <img src="img/wild-coast/map_wild_coast.png" alt="The Wild Coast close up: a narrow shelf with canyons just offshore">
    <figcaption>The Wild Coast close up: a narrow shelf, with canyons just offshore.</figcaption>
  </figure>
  <div class="side-text" markdown="1">
<div class="step" markdown="1">

### Canyons, not seamounts

The hypothesis holds. The Wild Coast's shelf is a narrow strip; only KwaZulu-Natal is as narrow. Two shelf-incising canyons come within 8 km of shore. Its deep-sea features are canyons cutting towards the coast, not seamounts.

</div>
<div class="step" markdown="1">

### What it cannot say

A narrow shelf brings the Agulhas Current and deep water close to the coast, and canyons can channel deep water and nutrients towards the shelf. Whether that shapes the Wild Coast's marine life, for example around the Pondoland Marine Protected Area, is a question this geomorphology alone cannot answer.

</div>
  </div>
</section>

<figure class="wide bleed">
  <img src="img/lab2/qgis_exo2_view.png" alt="QGIS view of the Lab 2 project: the Port St Johns canyons just south of the Pondoland MPA, with the Hluleka and Dwesa-Cwebe MPAs">
  <figcaption>Lab 2, <em>Map my place</em>: the two shelf-incising canyons off Port St Johns (filled orange) inside my place (yellow), just south of the Pondoland Marine Protected Area (green). Data: GSFM canyons, GRID-Arendal (CC BY 4.0); ProtectedSeas Navigator V2 (CC BY 4.0), via ODP; basemap © OpenStreetMap contributors.</figcaption>
</figure>

<div class="read" markdown="1">

## Where it led

Starting from a global seamount file, I found that the Wild Coast has none nearby, and went looking for what it has instead: canyons. My Lab 2 place is the Port St Johns canyons, just outside the Pondoland MPA. After the course, I plan a short [Zenodo article](learning-path.md#after-the-course-a-zenodo-article) on the Wild Coast seafloor.

<div class="actions" markdown="1">
[Read the ArcGIS story map](https://storymaps.arcgis.com/stories/4a21fdf0c85140f9b3fb6b648d483599){ .md-button .md-button--primary }
[The full exercise](module-2-wild-coast.md){ .md-button }
[Lab 2 in Module 2](module-2-gis.md#lab-2-port-st-johns-canyons){ .md-button }
</div>

</div>

<div class="read" markdown="1">

<span class="section-label">The course at a glance</span>

## Five steps to the certificate

There is a certificate for each module, and one for the whole course if all four modules are done by **Friday 18 December**. The dates and the closing webinar are on [Learning path](learning-path.md).

</div>

<div class="cards" markdown="1">
<div class="card done" markdown="1">
<span class="when">Tue 3 Nov</span>

#### [Welcome and Sign-up](welcome.md)

ODP account, the three areas of ODP, QGIS or ArcGIS installed.

<span class="badge">Done, 4 of 4 lessons</span>
</div>
<div class="card done" markdown="1">
<span class="when">Fri 13 Nov</span>

#### [1. Explore](module-1-explore.md)

Finding and looking at ocean data in the ODP Catalog.

<span class="badge">Done</span>
</div>
<div class="card done" markdown="1">
<span class="when">Thu 19 Nov</span>

#### [2. GIS](module-2-gis.md)

ODP data in QGIS or ArcGIS, Lab 2: Map my place.

<span class="badge">Done, certificate 22 Nov</span>
</div>
<div class="card next" markdown="1">
<span class="when">Thu 26 Nov</span>

#### [3. Code](module-3-code.md)

Notebooks in an ODP Workspace, Python or R.

<span class="badge">Not open yet</span>
</div>
<div class="card next" markdown="1">
<span class="when">Thu 3 Dec</span>

#### [4. Plan](module-4-plan.md)

Marine spatial planning in SeaSketch.

<span class="badge">Not open yet</span>
</div>
</div>

<div class="read" markdown="1">

<span class="section-label">Status</span>

## The log

</div>

<div class="timeline" markdown="1">
<div class="entry" markdown="1">
<span class="date">22 November 2026, late</span>
**Module 2 done**, certificate issued by HUB Ocean. Next, after the course: a Zenodo article on the Wild Coast seafloor, over the holidays. See [Learning path](learning-path.md#after-the-course-a-zenodo-article).
</div>
<div class="entry" markdown="1">
<span class="date">22 November 2026, night</span>
*From Download to Map* done in QGIS and in ArcGIS Online, 6 of 8 lessons. Lab 2 drawn: [Port St Johns canyons](module-2-gis.md#lab-2-port-st-johns-canyons), just outside the Pondoland MPA; upload to ODP next.
</div>
<div class="entry" markdown="1">
<span class="date">22 November 2026, evening</span>
The Wild Coast exercise as an [ArcGIS story map](https://storymaps.arcgis.com/stories/4a21fdf0c85140f9b3fb6b648d483599).
</div>
<div class="entry" markdown="1">
<span class="date">22 November 2026, afternoon</span>
Module 2 exercise, [The Wild Coast seafloor](module-2-wild-coast.md). The Wild Coast has no seamount within about 190 km; instead it has one of South Africa's narrowest shelves (median 14 km) and the most submarine canyons per 100 km of coast, the closest within 7 km of shore. Four ODP layers, a notebook, and QGIS. *Data formats and connections* and *Installing QGIS* done: 4 of 8 lessons.
</div>
<div class="entry" markdown="1">
<span class="date">22 November 2026</span>
Started [Module 2: GIS](module-2-gis.md). The first two lessons, *Welcome to GIS* and *Choose your tool: QGIS or ArcGIS*, are done. I am on *Data formats and connections*, with a global seamount dataset downloaded as CSV, GeoJSON and Parquet for its assignment.
</div>
<div class="entry" markdown="1">
<span class="date">Week of 9 November</span>
Signed up, finished *Welcome and Sign-up* and [Module 1: Explore](module-1-explore.md).
</div>
<div class="entry" markdown="1">
<span class="date">12 November 2026</span>
Opening webinar (recorded).
</div>
</div>

<div class="read" markdown="1">

Which format would you reach for first with ocean data: a file you download, or a live connection?

</div>

</div>
