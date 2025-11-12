import streamlit as st
from streamlit_extras.stylable_container import stylable_container
import streamlit_carousel

# items_carousel = [
#     dict(
#         img="https://i.imgur.com/ZnrNi2k.png",
#         title="ExcelOne",
#         text="",
#         img_style="height: 100%; width: 100%; object-fit: cover;",
#     ),
#     dict(
#         title="ProFinder 1",
#         text="",
#         img="https://i.imgur.com/23khe2T.jpeg",
#     ),
#     dict(
#         title="ProFinder 2",
#         text="",
#         img="https://i.imgur.com/4bACEjT.jpeg"
#     ),
#     dict(
#         title="ProFinder 3",
#         text="",
#         img="https://i.imgur.com/HOygDiO.jpeg",
#     ),
#     dict(
#         title="PPPoE",
#         text="",
#         img="https://i.imgur.com/pv02qVs.png",
#     ),
# ]


with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

with open("html_bio.html") as f:
    html_bio = f.read()

with open("html_excelone.html") as f:
    html_excelone = f.read()

with open("html_profinder.html") as f:
    html_profinder = f.read()

with open("html_pppoe.html") as f:
    html_pppoe = f.read()

st.set_page_config(page_icon="💻", page_title="Piodos Portfolio", layout="wide")

st.markdown('<div id="abt-me"></div>', unsafe_allow_html=True)

with st.container(horizontal=True, key="container_nav"):
    col1, col2, col3, col4, col5, col6 = st.columns([1, 1, 1, 1, 1, 5])

    nav_abt_me = col1.container()
    with nav_abt_me:
        st.markdown("""
                    <a href="#abt-me" style="color:white; text-decoration:none;">About Me</a>
                    """, unsafe_allow_html=True)

    nav_proj = col2.container()
    with nav_proj:
        st.markdown("""
                            <a href="#projects" style="color:white; text-decoration:none;">Projects</a>
                            """, unsafe_allow_html=True)

    nav_skills = col3.container()
    with nav_skills:
        st.markdown("""
                            <a href="#skills-and-programming-languages" style="color:white; text-decoration:none;">Skills</a>
                            """, unsafe_allow_html=True)
    nav_back = col4.container()
    with nav_back:
        st.markdown("""
                    <a href="#background" style="color:white; text-decoration:none;">Background</a>
                    """, unsafe_allow_html=True)

    nav_contacts = col5.container()
    with nav_contacts:
        st.markdown("""
                    <a href="#contacts" style="color:white; text-decoration:none;">Contacts</a>
                    """, unsafe_allow_html=True)


#About Me
abt_me_col1, abt_me_col2, abt_me_col3, abt_me_col4 = st.columns([0.2, 1, 3, 0.2])

with st.container():
    with abt_me_col2:
        with stylable_container(
                key="image_profile",
                css_styles="""
                    img {
                        border-radius: 40px;
                        height: 400px;
                        width: auto;    
                        margin-bottom: 30px;
                    }
                    """,
        ):
            st.image("Streamlit Assets/Josh.jpg")
    with abt_me_col3:
        st.markdown(html_bio, unsafe_allow_html=True)

st.markdown('<div id="projects"></div>', unsafe_allow_html=True)

#Projects
project_container = st.container(key="container_projects_main", horizontal_alignment="center", horizontal=True)

with project_container:
    spacer_1, prj_col1, prj_col2, prj_col3, spacer_2 = st.columns([0.15, 1, 1, 1, 0.1])

    #ExcelOne
    tile1 = prj_col1.container(height=520, width=380, key="container_excelone")
    with tile1:
        st.markdown(html_excelone, unsafe_allow_html=True)
        column_link, column_carousel = st.columns([5, 3.5])

        with column_link:
            st.markdown("""
                        <a class="btn_github" href="https://github.com/IgnisFrostburn/OOP-Capstone" style="text-decoration: none; color: white">View Github</a>
                        """, unsafe_allow_html=True)

    #ProFinder
    tile2 = prj_col2.container(height=520, width=380, key="container_profinder")
    with tile2:
        st.markdown(html_profinder, unsafe_allow_html=True)
        column_link, column_carousel = st.columns([7, 2])

        with column_link:
            st.markdown("""
                                <a class="btn_github" href="https://github.com/IgnisFrostburn/ProFinder" style="text-decoration: none; color: white">View Github</a>
                                """, unsafe_allow_html=True)

    #PPPoE
    tile3 = prj_col3.container(height=520, width=380, key="container_pppoe")
    with tile3:
        st.markdown(html_pppoe, unsafe_allow_html=True)
        column_link, column_carousel = st.columns([7, 2])

        with column_link:
            st.markdown("""
                                <a class="btn_github" href="https://github.com/Kintoyyy/CSIT228-Finals-JAVA_PPPoE_Management_System" style="text-decoration: none; color: white">View Github</a>
                                """, unsafe_allow_html=True)

#Project Carousel
# streamlit_carousel.carousel(items=items_carousel, container_height=500)



st.markdown("""
            <style>
                h2[data-anchor="skills-and-programming-languages"] {
                    visibility: hidden;
                    height: 0;
                    margin: 0;
                    padding: 0;
                }
            </style>
            ## Skills and Programming Languages""", unsafe_allow_html=True)

#Skills row 1
with st.container(horizontal_alignment="center", horizontal=True):
    skill_c, skill_cpp, skill_csharp, skill_java = st.columns([1, 1, 1, 1])

    skill_c_tile = skill_c.container(height=70, width=350, border=False, key="container_skill_c")
    with skill_c_tile:
        with stylable_container(
                key="image_skill_c",
                css_styles="""
                            img {
                                height: 50px;
                                width: auto;
                                margin-top: -30%;
                            }
                            """,
        ):
            st.image("Streamlit Assets/icon_c.png")
        st.markdown("""
                    <div class="container_skill_main">
                    <p class="skill_name" style="font-size: 1.7rem">C</p>
                    </div>""", unsafe_allow_html=True)

    skill_cpp_tile = skill_cpp.container(height=70, width=350, border=False, key="container_skill_cpp")
    with skill_cpp_tile:
        with stylable_container(
                key="image_skill_cpp",
                css_styles="""
                                img {
                                    height: 50px;
                                    width: auto;
                                    margin-top: -30%;
                                }
                                """,
        ):
            st.image("Streamlit Assets/icon_cpp.png")
        st.markdown("""
                    <div class="container_skill_main">
                    <p class="skill_name" style="font-size: 1.7rem">C++</p>
                    </div>""", unsafe_allow_html=True)

    skill_csharp_tile = skill_csharp.container(height=70, width=350, border=False, key="container_skill_csharp")
    with skill_csharp_tile:
        with stylable_container(
                key="image_skill_csharp",
                css_styles="""
                                    img {
                                        height: 50px;
                                        width: auto;
                                        margin-top: -30%;
                                    }
                                    """,
        ):
            st.image("Streamlit Assets/icon_csharp.png")
        st.markdown("""
                    <div class="container_skill_main">
                    <p class="skill_name" style="font-size: 1.7rem">C#</p>
                    </div>""", unsafe_allow_html=True)

    skill_java_tile = skill_java.container(height=70, width=350, border=False, key="container_skill_java")
    with skill_java_tile:
        with stylable_container(
                key="image_skill_java",
                css_styles="""
                                    img {
                                        height: 50px;
                                        width: auto;
                                        margin-top: -30%;
                                    }
                                    """,
        ):
            st.image("Streamlit Assets/icon_java.png")
        st.markdown("""
            <div class="container_skill_main">
            <p class="skill_name" style="font-size: 1.7rem">Java</p>
            </div>""", unsafe_allow_html=True)


#Skill row 2
with st.container(horizontal_alignment="center", horizontal=True):
    skill_sql, skill_python, skill_kotlin, skill_assembly = st.columns([1, 1, 1, 1])

    skill_sql_tile = skill_sql.container(height=70, width=350, border=False, key="container_skill_sql")
    with skill_sql_tile:
        with stylable_container(
                key="image_skill_sql",
                css_styles="""
                            img {
                                    height: 50px;
                                    width: auto;
                                    margin-top: -30%;
                            }
                            """,
        ):
            st.image("Streamlit Assets/icon_sql.png")
        st.markdown("""
                    <div class="container_skill_main">
                    <p class="skill_name" style="font-size: 1.7rem">SQL</p>
                    </div>""", unsafe_allow_html=True)

    skill_python_tile = skill_python.container(height=70, width=350, border=False, key="container_skill_python")
    with skill_python_tile:
        with stylable_container(
                key="image_skill_python",
                css_styles="""
                                img {
                                    height: 50px;
                                    width: auto;
                                    margin-top: -30%;
                                }
                                """,
        ):
            st.image("Streamlit Assets/icon_python.png")
        st.markdown("""
                    <div class="container_skill_main">
                    <p class="skill_name" style="font-size: 1.7rem">Python</p>
                    </div>""", unsafe_allow_html=True)

    skill_kotlin_tile = skill_kotlin.container(height=70, width=350, border=False, key="container_skill_kotlin")
    with skill_kotlin_tile:
        with stylable_container(
                key="image_skill_kotlin",
                css_styles="""
                                    img {
                                        height: 50px;
                                        width: auto;
                                        margin-top: -30%;
                                    }
                                    """,
        ):
            st.image("Streamlit Assets/icon_kotlin.png")
        st.markdown("""
                    <div class="container_skill_main">
                    <p class="skill_name" style="font-size: 1.7rem">Kotlin</p>
                    </div>""", unsafe_allow_html=True)

    skill_assembly_tile = skill_assembly.container(height=70, width=350, border=False, key="container_skill_assembly")
    with skill_assembly_tile:
        with stylable_container(
                key="image_skill_assembly",
                css_styles="""
                                    img {
                                        height: 50px;
                                        width: auto;
                                        margin-top: -30%;
                                    }
                                    """,
        ):
            st.image("Streamlit Assets/icon_asm.png")
        st.markdown("""
            <div class="container_skill_main">
            <p class="skill_name" style="font-size: 1.7rem">Assembly</p>
            </div>""", unsafe_allow_html=True)

#Skill row 3
with st.container(horizontal_alignment="center", horizontal=True):
    skill_html, skill_css, skill_js, skill_ml = st.columns([1, 1, 1, 1])

    skill_html_tile = skill_html.container(height=70, width=350, border=False, key="container_skill_html")
    with skill_html_tile:
        with stylable_container(
                key="image_skill_html",
                css_styles="""
                            img {
                                    height: 50px;
                                    width: auto;
                                    margin-top: -30%;
                            }
                            """,
        ):
            st.image("Streamlit Assets/icon_html.png")
        st.markdown("""
                    <div class="container_skill_main">
                    <p class="skill_name" style="font-size: 1.7rem">HTML</p>
                    </div>""", unsafe_allow_html=True)

    skill_css_tile = skill_css.container(height=70, width=350, border=False, key="container_skill_css")
    with skill_css_tile:
        with stylable_container(
                key="image_skill_css",
                css_styles="""
                                img {
                                    height: 50px;
                                    width: auto;
                                    margin-top: -30%;
                                }
                                """,
        ):
            st.image("Streamlit Assets/icon_css.png")
        st.markdown("""
                    <div class="container_skill_main">
                    <p class="skill_name" style="font-size: 1.7rem">CSS</p>
                    </div>""", unsafe_allow_html=True)

    skill_js_tile = skill_js.container(height=70, width=350, border=False, key="container_skill_js")
    with skill_js_tile:
        with stylable_container(
                key="image_skill_js",
                css_styles="""
                                    img {
                                        height: 50px;
                                        width: auto;
                                        margin-top: -30%;
                                    }
                                    """,
        ):
            st.image("Streamlit Assets/icon_js.png")
        st.markdown("""
                    <div class="container_skill_main">
                    <p class="skill_name" style="font-size: 1.7rem">JS  </p>
                    </div>""", unsafe_allow_html=True)

    skill_ml_tile = skill_ml.container(height=70, width=350, border=False, key="container_skill_ml")
    with skill_ml_tile:
        with stylable_container(
                key="image_skill_ml",
                css_styles="""
                                    img {
                                        height: 50px;
                                        width: auto;
                                        margin-top: -15%;
                                    }
                                    """,
        ):
            st.image("Streamlit Assets/icon_ml.png")
        st.markdown("""
            <div class="container_skill_main">
            <p class="skill_name" style="font-size: 1.7rem">MLBB</p>
            </div>""", unsafe_allow_html=True)

st.markdown('<div id="background"></div>', unsafe_allow_html=True)

#Background
with st.container(horizontal_alignment="center", horizontal=True):
    column_education, column_achievements = st.columns([1, 1])

    #Education
    with column_education:
        st.markdown("""
                    <p class="education_and_achievements" style="font-size: 2rem; margin-top: 200px;">Education</p>
                    <p class="dates" style="font-size: 0.9rem; margin-top: 20px;">2023-Present</p>
                    """, unsafe_allow_html=True)
        with st.container(horizontal_alignment="center", horizontal=True, height=100, key="container_citu"):
            column_spacer_citu, column_citu_logo, column_citu = st.columns([0.2, 1, 8])
            with column_citu_logo:
                with stylable_container(
                        key="image_citu",
                        css_styles="""
                                    img {
                                            height: 60px;
                                            margin-top: -20%;
                                    }
                                    """,
                ):
                    st.image("Streamlit Assets/icon_citu.png")
            with column_citu:
                st.markdown("""
                            <p class="school_name" style="font-size: clamp(0.5rem, 1vw, 1.3rem); margin-top: -2%;">CEBU INSTITUTE OF TECHNOLOGY - UNIVERSITY</p>
                            <p class="school_desc" style="font-size: clamp(0.5rem, 1vw, 1.3rem);">Bachelor of Science in Computer Science</p>
                            """, unsafe_allow_html=True)

        st.markdown("""
                    <p class="dates" style="font-size: 0.9rem;">2021-2023</p>
                    """, unsafe_allow_html=True)
        with st.container(horizontal_alignment="center", horizontal=True, height=100, key="container_onhs_shs"):
            column_spacer_citu, column_citu_logo, column_citu = st.columns([0.2, 1, 8])
            with column_citu_logo:
                with stylable_container(
                        key="image_onhs_shs",
                        css_styles="""
                                    img {
                                            height: 60px;
                                            margin-top: -20%;
                                    }
                                    """,
                ):
                    st.image("Streamlit Assets/icon_onhs.png")
            with column_citu:
                st.markdown("""
                            <p class="school_name" style="font-size: clamp(0.5rem, 1vw, 1.3rem); margin-top: -2%;">OCAÑA NATIONAL HIGH SCHOOL</p>
                            <p class="school_desc" style="font-size: clamp(0.5rem, 1vw, 1.3rem);">Senior High School - STEM</p>
                            """, unsafe_allow_html=True)

        st.markdown("""
                            <p class="dates" style="font-size: 0.9rem;">2017-2021</p>
                            """, unsafe_allow_html=True)
        with st.container(horizontal_alignment="center", horizontal=True, height=100, key="container_onhs_jhs"):
            column_spacer_citu, column_citu_logo, column_citu = st.columns([0.2, 1, 8])
            with column_citu_logo:
                with stylable_container(
                        key="image_onhs_jhs",
                        css_styles="""
                                            img {
                                                    height: 60px;
                                                    margin-top: -20%;
                                            }
                                            """,
                ):
                    st.image("Streamlit Assets/icon_onhs.png")
            with column_citu:
                st.markdown("""
                                    <p class="school_name" style="font-size: clamp(0.5rem, 1vw, 1.3rem); margin-top: -2%;">OCAÑA NATIONAL HIGH SCHOOL</p>
                                    <p class="school_desc" style="font-size: clamp(0.5rem, 1vw, 1.3rem);">Junior High School</p>
                                    """, unsafe_allow_html=True)

        st.markdown("""
                            <p class="dates" style="font-size: 0.9rem;">2021-2023</p>
                            """, unsafe_allow_html=True)
        with st.container(horizontal_alignment="center", horizontal=True, height=100, key="container_tes"):
            column_spacer_citu, column_citu_logo, column_citu = st.columns([0.2, 1, 8])
            with column_citu_logo:
                with stylable_container(
                        key="image_tes",
                        css_styles="""
                                            img {
                                                    height: 60px;
                                                    margin-top: -20%;
                                            }
                                            """,
                ):
                    st.image("Streamlit Assets/icon_tes.png")
            with column_citu:
                st.markdown("""
                                    <p class="school_name" style="font-size: clamp(0.5rem, 1vw, 1.3rem); margin-top: -2%;">TUYOM ELEMENTARY SCHOOL</p>
                                    <p class="school_desc" style="font-size: clamp(0.5rem, 1vw, 1.3rem);">Elementary School</p>
                                    """, unsafe_allow_html=True)

    #Achievements
    with column_achievements:
        st.markdown("""
                    <p class="education_and_achievements" style="font-size: 2rem; margin-top: 200px; margin-bottom: 30px;">Achievements</p>
                    """, unsafe_allow_html=True)
        with st.container(horizontal_alignment="center", horizontal=True, height=150, key="container_codechum"):
            column_achievements_image, column_achievements_desc = st.columns([2, 9])
            with column_achievements_image:
                with stylable_container(
                        key="image_codechum",
                        css_styles="""
                                            img {
                                                    height: 110px;
                                                    margin-top: 5px;
                                            }
                                            """,
                ):
                    st.image("Streamlit Assets/icon_codechum.jpg")

            with column_achievements_desc:
                st.markdown("""
                            <p class="achievement_name" style="font-size: clamp(0.5rem, 1.5vw, 1.7rem);">CodeChum C Certification and Java Certification Exams Passer</p>
                            <p class="achievement_desc" style="font-size: clamp(0.5rem, 1vw, 1.3rem);">I passed the C Certification and Java Certification Exams by CodeChum. I achieved Top 10 in both exams. </p>
                            """, unsafe_allow_html=True)

        with st.container(horizontal_alignment="center", horizontal=True, height=150, key="container_dost"):
            column_achievements_image, column_achievements_desc = st.columns([2, 9])
            with column_achievements_image:
                with stylable_container(
                        key="image_dost",
                        css_styles="""
                                            img {
                                                    height: 110px;
                                            }
                                            """,
                ):
                    st.image("Streamlit Assets/icon_dost.jpg")

            with column_achievements_desc:
                st.markdown("""
                            <p class="achievement_name" style="font-size: clamp(0.5rem, 1.5vw, 1.7rem);">DOST SEI Scholarship Student</p>
                            <p class="achievement_desc" style="font-size: clamp(0.5rem, 1vw, 1.3rem);">I passed the DOST SEI scholarship exam in 2023 and currently a DOST SEI scholar.</p>
                            """, unsafe_allow_html=True)

        with st.container(horizontal_alignment="center", horizontal=True, height=150, key="container_kalea"):
            column_achievements_image, column_achievements_desc = st.columns([2, 9])
            with column_achievements_image:
                with stylable_container(
                        key="image_kalea",
                        css_styles="""
                                            img {
                                                    height: 110px;
                                            }
                                            """,
                ):
                    st.image("Streamlit Assets/icon_kalea.webp")

            with column_achievements_desc:
                st.markdown("""
                            <p class="achievement_name" style="font-size: clamp(0.5rem, 1.5vw, 1.7rem);">Top 36 Cebu Kalea in Mobile Legends</p>
                            <p class="achievement_desc" style="font-size: clamp(0.5rem, 1vw, 1.3rem);">NO EXPLANATION NEEDED.</p>
                            """, unsafe_allow_html=True)

st.markdown('<div id="contacts"></div>', unsafe_allow_html=True)

#Contacts
with st.container(key="container_main_contacts"):
    st.markdown("""
                <p class="contact" style="font-size: clamp(2rem, 3vw, 4rem);"><span style="color:#FFC31E">Let's Get in Touch:</span> Ways to contact me</p>
                <p class="achievement_desc" style="font-size: clamp(0.5rem, 1vw, 1.3rem); margin-bottom: 20px;">If you have any inquiries, commissions, collaborations, etc., feel free to contact me through my different social accounts and contact info. I will do my best to reply within 24 hours, but it might take more than a day.</p>
                """, unsafe_allow_html=True)
    with st.container(horizontal_alignment="center", horizontal=True, height=50, key="container_fb", border=False):
        column_contact_image, column_contact_desc = st.columns([0.3, 9])
        with column_contact_image:
            with stylable_container(
                    key="image_fb",
                    css_styles="""
                                        img {
                                                height: 30px;
                                        }
                                        """,
            ):
                st.image("Streamlit Assets/icon_facebook.png")
            with column_contact_desc:
                st.markdown("""
                        <a href="https://www.facebook.com/josh.mark.piodos" class="contact_link" style="font-size: clamp(0.5rem, 1vw, 3rem); text-decoration: none; color: white;">Follow me on Facebook</a>
                        """, unsafe_allow_html=True)
    with st.container(horizontal_alignment="center", horizontal=True, height=50, key="container_ig", border=False):
        column_contact_image, column_contact_desc = st.columns([0.3, 9])
        with column_contact_image:
            with stylable_container(
                    key="image_ig",
                    css_styles="""
                                        img {
                                                height: 30px;
                                        }
                                        """,
            ):
                st.image("Streamlit Assets/icon_instagram.png")
            with column_contact_desc:
                st.markdown("""
                        <a href="https://www.instagram.com/chuuni_onii_chan/" class="contact_link" style="font-size: clamp(0.5rem, 1vw, 3rem); text-decoration: none; color: white;">Follow me on Instagram</a>
                        """, unsafe_allow_html=True)
    with st.container(horizontal_alignment="center", horizontal=True, height=50, key="container_mail", border=False):
        column_contact_image, column_contact_desc = st.columns([0.3, 9])
        with column_contact_image:
            with stylable_container(
                    key="image_mail",
                    css_styles="""
                                        img {
                                                height: 30px;
                                        }
                                        """,
            ):
                st.image("Streamlit Assets/icon_mail.png")
            with column_contact_desc:
                st.markdown("""
                        <a href="" class="contact_link" style="font-size: clamp(0.5rem, 1vw, 3rem); text-decoration: none; color: white;">joshmark.piodos@cit.edu</a>
                        """, unsafe_allow_html=True)

    with st.container(horizontal_alignment="center", horizontal=True, height=50, key="container_phone", border=False):
        column_contact_image, column_contact_desc = st.columns([0.3, 9])
        with column_contact_image:
            with stylable_container(
                    key="image_phone",
                    css_styles="""
                                        img {
                                                height: 30px;
                                        }
                                        """,
            ):
                st.image("Streamlit Assets/icon_phone.png")
            with column_contact_desc:
                st.markdown("""
                        <a href="" class="contact_link" style="font-size: clamp(0.5rem, 1vw, 3rem); text-decoration: none; color: white;">+63 981 794 3565</a>
                        """, unsafe_allow_html=True)

    with st.container(horizontal_alignment="center", horizontal=True, height=100, key="container_copyright", border=False):
        st.markdown("""
                    <p style="font-size: clamp(0.5rem, 1vw, 3rem); padding-top: 50px;">© 2025 Josh Mark Piodos. All Rights Reserved</a>
                    """, unsafe_allow_html=True)












