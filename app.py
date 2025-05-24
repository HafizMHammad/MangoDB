import streamlit as st
from blast import blast_ui
from msa import msa_ui
from pathlib import Path

st.set_page_config(page_title="Mango Genome Database")
def app_header():
    # Use columns to place logo on left, text on right
    col1, col2, col3 = st.columns([3, 6, 3])  # Adjust ratio as needed

    with col1:
        st.image("static/SSUETLogo.png", width=130)  # your app logo here

    with col2:
        st.markdown("""
            # Mango Genome Database
        """)
       
    with col3:
        st.image("logo.png", width=125)  # your app logo here

def app_footer():
    # Footer with link centered
    st.markdown("---")  # horizontal line
    st.markdown(
        """
        <p style="text-align: center; font-size: 12px;">
        Developed by <strong><a href="https://www.bioinfoquant.com" target="_blank">BioInfoQuant</a></strong>, 
        </p>
        """,
        unsafe_allow_html=True
    )

app_header()
col1, col2, col3 = st.columns([3, 6, 3])
with col2:
   st.markdown("""
            **Department of Bioinformatics**  
            Sir Syed University of Engineering & Technology  
            University Road, Karachi-75300, Pakistan
        """)

# Sidebar structure with grouped items
st.markdown(
    """
    <style>
    /* Target sidebar radio option labels */
    div[data-testid="stSidebar"] label {
        font-size: 20px !important;
        font-weight: 600;
    }
    </style>
    """,
    unsafe_allow_html=True
)

sidebar_main = st.sidebar.radio("Menu", ["BLAST", "MSA", "Downloads", "About", "Help"])
choice = None

if sidebar_main == "About":
    about_choice = st.sidebar.selectbox("About", ["Project", "Disclaimer", "Work", "Literature"])
    choice = f"About - {about_choice}"
elif sidebar_main == "Help":
    help_choice = st.sidebar.selectbox("Help", ["Contact Us", "User Guide"])
    choice = f"Help - {help_choice}"
else:
    choice = sidebar_main

images = Path("images")

# Now content logic based on choice
if choice == "About - Project":
    st.title("Mango Genome Database and Big Data Analysis Tool")

    st.write("""
    Mango is the fifth most important subtropical/tropical fruit crop worldwide with production centered in India and South East Asia. Due to the difficulty of specific pollination, mango breeding is still predominantly the selection of trees with superior fruit traits rather than hybrid production and evaluation. Recently, there has been a worldwide interest in mango genomics to produce tools for Marker Assisted Selection and trait association. There are five transcriptomes produced respectively in Israel, India, Mexico, Pakistan and the US.

    Our project "Mango Genome Database" is constructed upon the completion of the Pakistan mango leaf transcriptome and chloroplast genome sequencing with the aim of providing the scientific community with accurate data and annotation of the mango genome sequence. Mango Genome Database contains annotated data including unigene of whole genome sequence of specie *Mangifera indica* L. (mango). The information contains predicted genes of the whole genome sequences and the unigenes are annotated in other species, KEGG pathway terms, providing a glimpse of the pathways and traits in which they are involved.

    The annotated sequence data can be browsed through the Gene Search page or queried using various categories in the search sites. The whole genome sequences can also be accessed and downloaded through Genome View. Some genetic information will be available through different sections in the database. Mango Genome Database also provides online analysis tools such as Blast server for the Mango datasets, a sequence or gene search server, and Genome view detection tools.
    """)

    st.subheader("Purpose")
    st.write("""
    Fruit Science is one of the important sectors of agriculture. With the growing population, demand for fruits is gradually increasing. One of the most important challenges in many fruit species is the unavailability of well-defined genetic studies. There is no database available for the Mango genome; thus, this particular platform will provide data and information about *Mangifera indica* L. cultivars from different countries and allow users to analyze their own data against our databases for many applications.
    """)

    st.subheader("Responsive Gallery")
    st.markdown("### Mango Genome of specie *Mangifera indica* L.")

    # Use columns to create a responsive gallery
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.image("static/Images/s1.jpg", caption='Mango (*Mangifera indica* L.) is called “king of fruits" in Pakistan.', use_column_width=True)
    with col2:
        st.image("static/Images/fc.jpg", caption='The Experimental procedure done at ICCBS (UoK).', use_column_width=True)
    with col3:
        st.image("static/Images/s3.jpg", caption='Sir Syed University of Engineering and Technology, Karachi.', use_column_width=True)
    with col4:
        st.image("static/Images/s4.jpg", caption='Mango Genome Database online project 2017.\nSir Syed University of Engineering and Technology, Karachi.', use_column_width=True)


elif choice == "About - Disclaimer":
    st.title("Disclaimer")
    st.markdown("""
    The information contained in this website is provided for general public, researchers, educators and students which is generated by the MGD team and gathered from different resources. While we endeavor to keep the information up to date and correct, we make no representations or warranties of any kind, express or implied, about the completeness, accuracy, reliability, suitability or availability with respect to the website or the information or related graphics contained on the website for any purpose. Any reliance you place on such information is therefore strictly at your own risk. In no event will we be liable for any loss or damage including without limitation, indirect or consequential loss or damage, or any loss or damage whatsoever arising from loss of data or profits arising out of, or in connection with, the use of this website.

    Through this website you are able to link to other websites which are not under the control of Mango Genome Database. We have no control over the nature, content and availability of those sites. The inclusion of any links does not necessarily imply a recommendation or endorse the views expressed within them.

    Every effort is made to keep the website up and running smoothly. However, MGD team takes no responsibility for, and will not be liable for, the website being temporarily unavailable due to technical issues beyond our control.
    """)


elif choice == "About - Work":
    st.title("Mango Genome Database")
    
    st.subheader("Objective and Purpose of Website")
    st.write("""
    To create the first website particularly for Mango Genome and the first-ever Pakistani website which will provide the scientific community and general public with bioinformatics resources related to Mango genomic sequence information and bioinformatics tools for retrieval and analysis of genomic sequences of different Mango cultivars (varieties).
    """)

    st.subheader("Relevant Background Information")
    st.write("""
    Mango, being the most important subtropical/tropical fruit crop, stands at the fifth position worldwide with major production in India and South-East Asia. Due to difficulties in fertilization, mango cultivation still relies mainly on natural selection rather than hybridization and evaluation. Recently, mango genomics has become a worldwide interest to generate tools for Marker Assisted Selection and trait association which require bioinformatics knowledge. Although large data on the Mango Genome have been reported by many countries since 2014, no dedicated platform was established specifically for mango to make this valuable data available to the scientific community.
    """)

    st.subheader("Scope of the Work")
    st.write("""
    Fruit Science is an important sector of agriculture. With the growing population, demand for fruits is gradually increasing. One of the major challenges in many fruit species is the lack of well-defined genetic studies. This website contains analyzed information of Mango Genome datasets of different cultivars and consists of many useful tools that provide accurate and useful results for research, academic work, development, analysis, and other biological needs.
    """)

    st.subheader("Timeline")
    st.write("""
    The whole project was developed within one year, including planning, analysis, development, and testing.
    """)

    st.subheader("Experience and Qualifications")
    st.write("""
    - **Expert:** Dr. Kamran Azim — Professor, Dean (Faculty of Life Sciences), HOD (Biosciences)  
    - **Senior:** Dr. Uzma Mehmood — Assistant Professor, HOD (Bioinformatics)  
    - **Senior:** Ms. Rabia Faizan — Lecturer, Bioinformatics  
    """)


elif choice == "About - Literature":
    st.title("Literature")
    st.markdown("""
    ### About Mango
    Mango is known as the “The king of the fruits," because it is nutritionally rich with unique flavor, taste, health-promoting qualities and aroma making it superior among new functional foods, often labeled as “super fruits”. This exotic fruit belongs to the family of Anacardiaceae — a family that also includes numerous species of tropical fruiting trees in the flowering plants such as cashew, pistachio.

    ### Mango Aroma
    Aroma is a complex mixture of a large number of volatile compounds, whose composition is specific to species and often to the variety of fruit. The most important aroma compounds include amino acid-derived compounds, lipid-derived compounds, phenolic derivatives, and mono- and sesquiterpenes. Mango (Mangifera indica L.) possesses a very attractive flavor characteristic. More than 270 aroma volatile compounds in different mango varieties have been identified in free form. Monoterpenes are the most important compounds contributing to mango flavor. Generally, terpenes are the major class of compounds in New World and Colombian mangoes whereas alcohols, ketones, and esters are mainly responsible for the characteristic aroma of Old World mangoes.

    ### Aroma Compounds
    Mango aroma is mainly formed by a complex mixture of compounds, but some authors consider terpenes, especially δ-3-carene, as the most important aroma constituents, due to the high percentage in the volatile fraction. The terpene hydrocarbons are considered to be important contributors to the flavour of Florida, Brazilian and Venezuelan mango varieties, Florida mango varieties, such as Keitt, Kent and Tommy Atkins, and 20 varieties of Cuban mangoes. In contrast, some varieties have considerable amounts of oxygenated volatile compounds, such as esters, furanones and lactones.

    The hydrocarbons (Z)- and (E)-â-ocimene have a warm, herbaceous, and floral odor, whereas the odor of δ-3-carene was sweet, reminiscent of refined limonene. Myrcene and (Z)-â-ocimene were reported to be responsible for the green aroma of raw mangos. The compound δ-3-carene was considered to be the major aroma-contributing component in some mangos, whereas the green aroma note typical of mango was correlated to monoterpene hydrocarbons. Taking into account the strong and characteristic aromas of monoterpene hydrocarbons, the simple differences partly explain the known differences in flavor among the Cuban cultivars.

    Among the sesquiterpene hydrocarbons, â-caryophyllene, R-humulene, and eremophilene were found to predominate in almost all Cuban cultivars. The first two compounds have also been found in significant quantities in other mangos. Eremophilene, the principal volatile compound ascribed to the African mango, was also found in some studied cultivars, whereas it could not be found in Brazilian fruits. The compound â-selinene, which was detected in considerable amount in Venezuelan fruit, in Willard and Parrot cultivars, and in African cultivars, was found in significant amount in only the Kent mango.

    The next class in importance after the terpene hydrocarbons was that of the esters, totaling 90 aliphatic, 16 aromatic, and 8 terpene esters found. Lactones, as intramolecular esters of 4- and 5-hydroxy acids, were also detected. 79 carbonyls were also identified.

    ### Mango Flavor
    Flavor volatiles are derived from an array of compounds including phytonutrients such as fatty acids, amino acids, carotenoids, phenols and terpenoids. Fruit volatile compounds are mainly comprised of diverse classes of chemicals, including esters, alcohols, aldehydes, ketones, lactones, and terpenoids. However, some sulfur compounds, such as S-methyl thiobutanoate, 3-(methylthio) propanal, 2-(methylthio) ethyl acetate, 3-(methylthio) ethyl propanoate, and 3-(methylthio) propyl acetate, also contribute to the flavor of fruit.

    Volatile terpenoid compounds, potentially derived from carotenoids, are important components of flavor and aroma in many fruits. Of particular interest are a group of terpenoid flavor volatile compounds generally present at relatively low levels but possessing strong effects on the overall human appreciation.

    ### Flavor Compounds
    Mango (Mangifera indica L.) possesses a very attractive flavor characteristic. More than 270 aroma volatile compounds in different mango varieties have been identified in free form. However, application of distillation extraction in combination with active odor value (aroma threshold) technologies exhibits that monoterpenes such as α-pinene, myrcene, α-phelladrene, σ-3-carene, p-cymene, limonene and terpinolene, esters including ethyl-2-methyl propanoate, ethyl butanoate, as well as (E,Z)-2,6-nonadienal, (E)-2-nonenal, methyl benzoate, (E)-β-ionone, decanal, and 2,5-dimethyl-4-methoxy-3(2H)-furanone are the most important compounds contributing to mango flavor.

    The hydrocarbons (Z)- and (E)-â-ocimene have a warm, herbaceous, and floral odor, whereas the odor of δ-3-carene was sweet, reminiscent of refined limonene. Myrcene and (Z)-â-ocimene were reported to be responsible for the green aroma of raw mangos. The compound δ-3-carene was considered to be the major aroma-contributing component in some mangos, whereas the green aroma note typical of mango was correlated to monoterpene hydrocarbons. Taking into account the strong and characteristic aromas of monoterpene hydrocarbons, the simple differences partly explain the known differences in flavor among the Cuban cultivars.

    Among the sesquiterpene hydrocarbons, â-caryophyllene, R-humulene, and eremophilene were found to predominate in almost all Cuban cultivars. The first two compounds have also been found in significant quantities in other mangos. Eremophilene, the principal volatile compound ascribed to the African mango, was also found in some studied cultivars, whereas it could not be found in Brazilian fruits. The compound â-selinene, which was detected in considerable amount in Venezuelan fruit, in Willard and Parrot cultivars, and in African cultivars, was found in significant amount in only the Kent mango.

    The next class in importance after the terpene hydrocarbons was that of the esters, totaling 90 aliphatic, 16 aromatic, and 8 terpene esters found. Lactones, as intramolecular esters of 4- and 5-hydroxy acids, were also detected. 79 carbonyls were also identified.

    ### References
    - Muna Ahmed Mohamed El Hadi, F.-J. Z., Fei-Fei Wu, Chun-Hua Zhou & Jun Tao. (2013). Advances in Fruit Aroma Volatile Research. *Molecules*, 18, 8200-8229.
    - Pino, J. A., Mesa, J., Munoz, Y., Marti, M. P., & Marbot, R. (2005). Volatile components from mango (Mangifera indica L.) cultivars. *J Agric Food Chem*, 53(6), 2213-2223.
    - T.M.M. Malundo, R. L. S., G.O. Ware, E.A. Baldwin. (2001). Sugars and Acids Influence Flavor Properties of Mango (Mangifera indica). *126*(1), 115–121.
    - Clara E. Quijano, G. S., Jorge A. Pino. (2007). Aroma volatile constituents of Colombian varieties of mango (Mangifera indica L.). *Flavour and Fragrance*, 22, 401–406.
    - Jorge A. Pino, J. M., †Yamilie Muñoz,†M. Pilar Martí,‡ and Rolando Marbot§. (2005). Volatile Components from Mango (Mangifera indica L.) Cultivars. *53* (6), 2213–2223.
    """)

elif choice == "Help - Contact Us":
    st.title("Contact Us")
    st.markdown("""
    **For any Query please contact**

    **Contact Information**

    Department of Bioinformatics,  
    Sir Syed University of Engineering & Technology,  
    University Road, Karachi-75300, Pakistan

    **Email:** qamartayyaba@yahoo.com

    **Phone:** +92 336 2808926

    ---

    **Developed by BioInfoQuant** 
     
    **Email:** contact@bioinfoquant.com  
    **Phone:** +92 339 4116531
    """)

elif choice == "Help - User Guide":
    st.title("User Guide")
    st.markdown("""
    Welcome to the **Mango Genome Database** user guide. This guide will help you navigate through the application and make the most out of its features.

    ## Sidebar Menu Overview

    The app has a sidebar menu with the following options:

    ### 1. BLAST
    - Perform sequence similarity searches.
    - You can either **paste your sequence** directly or **upload a FASTA file**.
    - Select the BLAST type:
        - `blastn` for nucleotide sequences.
        - `blastp` for protein sequences.
    - Choose a database from:
        - **All Genomes** (combines all available genome datasets),
        - or select specific genome or proteome databases.
    - The BLAST results are displayed as a table with detailed hit information.
    - Download the results as CSV or TSV files.
    - Visualize alignment statistics with downloadable plots such as identity distribution, E-value distribution, and bit scores.

    ### 2. MSA (Multiple Sequence Alignment)
    - Paste sequence data for alignment.
    - Align multiple sequences to find conserved regions and differences.
    - Download alignment results in CSV/TSV format.
    - Visualize and download alignment plots.

    ### 3. Downloads
    - Access mango genome and transcriptome datasets.
    - Download reference genome sequences, annotated gene sets, and other relevant data.

    ### 4. About
    - Learn about the project background, objectives, and contributors.
    - Read the disclaimer and relevant literature references.

    ### 5. Help
    - Access this User Guide.
    - Contact information for further assistance.

    ## How to Use BLAST Tool

    1. Navigate to the **BLAST** tab from the sidebar.
    2. Paste your query sequence or upload a FASTA file.
    3. Select BLAST type (`blastn` or `blastp`) depending on your query sequence.
    4. Choose the target database to search against.
    5. Click **Run BLAST** to start the search.
    6. View the tabular results and download your preferred output format.
    7. Explore the plotted statistics to analyze your results visually.

    ## How to Use MSA Tool

    1. Go to the **MSA** tab.
    2. Paste multiple sequences in FASTA format.
    3. Run the alignment.
    4. Review the aligned sequences.
    5. Download the alignment file and any generated plots.

    ## Downloading Data and Results

    - All results from BLAST and MSA tools can be downloaded in **CSV** or **TSV** formats.
    - Plots generated during analysis can be downloaded as **PNG images** for further inspection or publication.

    For any additional support, please visit the **Help - Contact Us** section or contact the development team.

    ---
    Thank you for using the **Mango Genome Database**!
    """)


elif choice == "BLAST":
    #st.title("BLAST Tool")
    # Call your BLAST function here
    blast_ui()

elif choice == "MSA":
    #st.title("MSA Tool")
    # Call your MSA function here
    msa_ui()

elif choice == "Downloads":
    st.title("Downloads")
    st.markdown("""
    - [CHINAZILL Nucleotide (FASTA)](data/CHINAZILLNUCLEOTIDE.fasta)  
    - [CHINAZILL Protein (FASTA)](data/CHINAZILLPROTEIN.fasta)  
    - [MEXICO KENT Nucleotide (FASTA)](data/MEXICOKENTNUCLEOTIDE.fasta)  
    - [MEXICO KENT Protein (FASTA)](data/MEXICOKENTPROTEIN.fasta)  
    - [ISRAEL KEITT Nucleotide (FASTA)](data/ISRAELKEITTNUCLEOTIDE.fasta)  
    - [ISRAEL KEITT Protein (FASTA)](data/ISRAELKEITTPROTEIN.fasta)  
    - [PAK MOD Nucleotide (FASTA)](data/Pakmod.fasta)  
    - [PAK Protein (FASTA)](data/PAKPROT.fasta)  
    - [PAKISTAN LANGRA (FASTA)](data/PAKISTANLANGRA.fasta)  
    - [Nucleotide and Protein FASTA (ZIP)](data/nucleotide_protein_fasta.zip)
    """)

app_footer()
