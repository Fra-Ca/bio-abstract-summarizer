import json
from anthropic import Anthropic
import os

client = Anthropic()

system_prompt = """You are a biomedical research assistant. Given a paper abstract, extract and return ONLY a valid JSON object with the following fields:
- condition: the disease or condition being studied
- study_type: the type of study
- sample_size: number of patients or subjects as an integer
- methodology: brief description of how the study was conducted
- key_findings: a list of the main findings
- clinical_relevance: why these findings matter clinically

Return only raw JSON, no other text, no markdown, no backticks. Start your response with { and end with }.
"""

abstract = """ Breast cancer is a disease encompassing a spectrum of molecular subtypes and clinical presentations, each with distinct prognostic implications and treatment responses. Breast cancer has traditionally been considered an immunologically "cold" tumor, unresponsive to immunotherapy. However, clinical trials in recent years have found immunotherapy to be an efficacious therapeutic option for select patients. Breast cancer is categorized into different subtypes ranging from the most common positive hormone receptor (HR+), human epidermal growth factor receptor 2 (HER2)-negative type, to less frequent HER2- positive breast cancer and triple-negative breast cancer (TNBC), highlighting the necessity for tailored treatment strategies aimed at maximizing patient outcomes. Despite notable progress in early detection and new therapeutic modalities, breast cancer remains the second leading cause of cancer death in the USA. Moreover, in recent decades, breast cancer incidence rates have been increasing, especially in women younger than the age of 50. This has prompted the exploration of new therapeutic approaches to address this trend, offering new therapeutic prospects for breast cancer patients. Immunotherapy is a class of therapeutic agents that has revolutionized the treatment landscape of many cancers, namely melanoma, lung cancer, and gastroesophageal cancers, amongst others. Though belatedly, immunotherapy has entered the treatment armamentarium of breast cancer, with the approval of pembrolizumab in combination with chemotherapy in triple-negative breast cancer (TNBC) in the neoadjuvant and advanced settings, thereby paving the path for further research and integration of immune checkpoint inhibitors in other subtypes of breast cancer. Trials exploring various combination therapies to harness the power of immunotherapy in symbiosis with various chemotherapeutic agents are ongoing in hopes of improving response rates and prolonging survival for breast cancer patients. Biomarkers and precise patient selection for the utilization of immunotherapy remain cardinal and are currently under investigation, with some biomarkers showing promise, such as Program Death Lignat-1 (PDL-1) Combined Positive Score, Tumor Mutation Burden (TMB), and Tumor Infiltrating Lymphocytes (TILs). This review will present the current landscape of immunotherapy, particularly checkpoint inhibitors, in different types of breast cancer. """

message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    system=system_prompt,
    messages=[{"role": "user", "content": abstract}]
)
raw = message.content[0].text
result = json.loads(raw)
print(json.dumps(result, indent=2))
