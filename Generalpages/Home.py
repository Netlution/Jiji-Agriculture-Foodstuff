# import streamlit as st
# import numpy as np
# import pandas as pd
# import base64

# st.markdown("""
# <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">""", unsafe_allow_html=True)
# st.markdown("""
# <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>""", unsafe_allow_html=True)

# st.markdown("""
# <nav class="navbar navbar-expand-lg navbar-light bg-light" style="background-color: blue;margin-top: -70px;">
#   <div class="container-fluid" >
#     <a class="navbar-brand" href="https://streamlit.io/">Streamlit</a>
#     <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
#       <span class="navbar-toggler-icon"></span>
#     </button>
#     <div class="collapse navbar-collapse" id="navbarNav">
#       <ul class="navbar-nav">
#         <li class="nav-item">
#           <a class="nav-link active" aria-current="page" href="https://streamlit.io/gallery">Gallery</a>
#         </li>
#         <li class="nav-item">
#           <a class="nav-link" href="https://streamlit.io/components">Components</a>
#         </li>
#         <li class="nav-item">
#           <a class="nav-link" href="https://streamlit.io/cloud">Cloud</a>
#         </li>
#         <li class="nav-item">
#           <a class="nav-link" href="https://streamlit.io/community" tabindex="-1">Community</a>
#         </li>
#       </ul>
#     </div>
#   </div>
# </nav>
# """, unsafe_allow_html=True)


# # SIDEBAR
# About = st.Page(page="pages/about.py",
#                 title="About page",
#                 icon="🅰️",
#                 # default=True,
#                 )
# Analysis = st.Page(page="pages/Analysis.py",
#                 title="Analysis page",
#                 icon="📈",
#               )

# Visualization = st.Page(page="pages/Visualization.py",
#                 title="Visualization page",
#                 icon="Ⓜ️"
#                 )

# Contact = st.Page(page="pages/Contact.py",
#                 title="Contact page",
#                 icon="🏦"
#                 )

# pg = st.navigation([About, Analysis, Visualization, Contact])

# pg.run()

import streamlit as st
import numpy as np
import pandas as pd
import base64

# ========== CUSTOM CSS ==========
sidebar_bg = """
<style>
[data-testid="stSidebar"] {
    background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), 
                url("https://images.unsplash.com/photo-1602621951019-1b8ca8f9e7d9");
    background-size: cover;
    background-position: center;
}
[data-testid="stSidebar"] * {
    color: white !important;
}
</style>
"""

st.markdown(sidebar_bg, unsafe_allow_html=True)


# ========== BOOTSTRAP NAVBAR ==========
st.markdown("""
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" 
rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
""", unsafe_allow_html=True)

st.markdown("""
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" 
integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
""", unsafe_allow_html=True)

st.markdown("""
<nav class="navbar navbar-expand-lg navbar-light bg-light" style="background-color: blue;margin-top: -70px;">
  <div class="container-fluid" >
    <a class="navbar-brand" href="https://streamlit.io/">Streamlit</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" 
    aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item"><a class="nav-link active" aria-current="page" href="https://streamlit.io/gallery">Gallery</a></li>
        <li class="nav-item"><a class="nav-link" href="https://streamlit.io/components">Components</a></li>
        <li class="nav-item"><a class="nav-link" href="https://streamlit.io/cloud">Cloud</a></li>
        <li class="nav-item"><a class="nav-link" href="https://streamlit.io/community" tabindex="-1">Community</a></li>
      </ul>
    </div>
  </div>
</nav>
""", unsafe_allow_html=True)


# ========== SIDEBAR NAVIGATION ==========
About = st.Page(page="pages/about.py", title="About", icon="🅰️")
Analysis = st.Page(page="pages/Analysis.py", title="Analysis", icon="📈")
Visualization = st.Page(page="pages/Visualization.py", title="Visualization", icon="Ⓜ️")
Contact = st.Page(page="pages/Contact.py", title="Contact", icon="🏦")

pg = st.navigation([About, Analysis, Visualization, Contact])
pg.run()
