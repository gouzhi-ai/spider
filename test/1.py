#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/12/13 上午9:47
# @Author  : 苏玉恒
# @File    : 1.py
# @Software: PyCharm

from bs4 import BeautifulSoup
import json

# 假设 html_content 是你提供的 HTML 文本
html_content = """<!DOCTYPE html>
<html lang="es" data-capo="">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
        <title>simplify 169^{-1 &#x2F;2}</title>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
        <script src="/mathquill.js"></script>
        <script src="/one-trust-utilities.js"></script>
        <script src="https://cdn.cookielaw.org/consent/28cd3f47-fef1-4429-be4b-ff2acc7f492b/OtAutoBlock.js" data-document-language="true"></script>
        <script src="https://cdn.cookielaw.org/scripttemplates/otSDKStub.js" data-domain-script="28cd3f47-fef1-4429-be4b-ff2acc7f492b" data-document-language="true"></script>
        <link rel="stylesheet" href="/mathquill.css">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css" integrity="sha384-nB0miv6/jRmo5UMMR1wu3Gz6NLsoTkbqJghGIsx//Rlm+ZU03BU6SQNC66uf4l5+" crossorigin="anonymous">
        <style>
            @font-face {
                font-display: swap;
                font-family: Ubuntu;
                font-style: italic;
                font-weight: 300;
                src: url(https://fonts.gstatic.com/s/ubuntu/v15/4iCp6KVjbNBYlgoKejZftVyCN4FNgYUJ31U.woff2) format("woff2");
                unicode-range: u+0460-052f,u+1c80-1c88,u+20b4,u+2de0-2dff,u+a640-a69f,u+fe2e-fe2f
            }

            @font-face {
                font-display: swap;
                font-family: Ubuntu;
                font-style: italic;
                font-weight: 300;
                src: url(https://fonts.gstatic.com/s/ubuntu/v15/4iCp6KVjbNBYlgoKejZftVyLN4FNgYUJ31U.woff2) format("woff2");
                unicode-range: u+0400-045f,u+0490-0491,u+04b0-04b1,u+2116
            }

            @font-face {
                font-display: swap;
                font-family: Ubuntu;
                font-style: italic;
                font-weight: 300;
                src: url(https://fonts.gstatic.com/s/ubuntu/v15/4iCp6KVjbNBYlgoKejZftVyDN4FNgYUJ31U.woff2) format("woff2");
                unicode-range: u+1f??
            }

            @font-face {
                font-display: swap;
                font-family: Ubuntu;
                font-style: italic;
                font-weight: 300;
                src: url(https://fonts.gstatic.com/s/ubuntu/v15/4iCp6KVjbNBYlgoKejZftVyMN4FNgYUJ31U.woff2) format("woff2");
                unicode-range: u+0370-03ff
            }

            @font-face {
                font-display: swap;
                font-family: Ubuntu;
                font-style: italic;
                font-weight: 300;
                src: url(https://fonts.gstatic.com/s/ubuntu/v15/4iCp6KVjbNBYlgoKejZftVyBN4FNgYUJ31U.woff2) format("woff2");
                unicode-range: u+0100-024f,u+0259,u+1e??,u+2020,u+20a0-20ab,u+20ad-20cf,u+2113,u+2c60-2c7f,u+a720-a7ff
            }

            @font-face {
                font-display: swap;
                font-family: Ubuntu;
                font-style: italic;
                font-weight: 300;
                src: url(https://fonts.gstatic.com/s/ubuntu/v15/4iCp6KVjbNBYlgoKejZftVyPN4FNgYUJ.woff2) format("woff2");
                unicode-range: u+00??,u+0131,u+0152-0153,u+02bb-02bc,u+02c6,u+02da,u+02dc,u+2000-206f,u+2074,u+20ac,u+2122,u+2191,u+2193,u+2212,u+2215,u+feff,u+fffd
            }

            @font-face {
                font-display: swap;
                font-family: Ubuntu;
                font-style: italic;
                font-weight: 400;
                src: url(https://fonts.gstatic.com/s/ubuntu/v15/4iCu6KVjbNBYlgoKej75l0miFYxnu4w.woff2) format("woff2");
                unicode-range: u+0460-052f,u+1c80-1c88,u+20b4,u+2de0-2dff,u+a640-a69f,u+fe2e-fe2f
            }

            @font-face {
                font-display: swap;
                font-family: Ubuntu;
                font-style: italic;
                font-weight: 400;
                src: url(https://fonts.gstatic.com/s/ubuntu/v15/4iCu6KVjbNBYlgoKej7wl0miFYxnu4w.woff2) format("woff2");
                unicode-range: u+0400-045f,u+0490-0491,u+04b0-04b1,u+2116
            }

            @font-face {
                font-display: swap;
                font-family: Ubuntu;
                font-style: italic;
                font-weight: 400;
                src: url(https://fonts.gstatic.com/s/ubuntu/v15/4iCu6KVjbNBYlgoKej74l0miFYxnu4w.woff2) format("woff2");
                unicode-range: u+1f??
            }

            @font-face {
                font-display: swap;
                font-family: Ubuntu;
                font-style: italic;
                font-weight: 400;
                src: url(https://fonts.gstatic.com/s/ubuntu/v15/4iCu6KVjbNBYlgoKej73l0miFYxnu4w.woff2) format("woff2");
                unicode-range: u+0370-03ff
            }

            @font-face {
                font-display: swap;
                font-family: Ubuntu;
                font-style: italic;
                font-weight: 400;
                src: url(https://fonts.gstatic.com/s/ubuntu/v15/4iCu6KVjbNBYlgoKej76l0miFYxnu4w.woff2) format("woff2");
                unicode-range: u+0100-024f,u+0259,u+1e??,u+2020,u+20a0-20ab,u+20ad-20cf,u+2113,u+2c60-2c7f,u+a720-a7ff
            }

            @font-face {
                font-display: swap;
                font-family: Ubuntu;
                font-style: italic;
                font-weight: 400;
                src: url(https://fonts.gstatic.com/s/ubuntu/v15/4iCu6KVjbNBYlgoKej70l0miFYxn.woff2) format("woff2");
                unicode-range: u+00??,u+0131,u+0152-0153,u+02bb-02bc,u+02c6,u+02da,u+02dc,u+2000-206f,u+2074,u+20ac,u+2122,u+2191,u+2193,u+2212,u+2215,u+feff,u+fffd
            }

            @font-face {
                font-display: swap;
                font-family: Ubuntu;
                font-style: italic;
                font-weight: 500;
                src: url(https://fonts.gstatic.com/s/ubuntu/v20/4iCp6KVjbNBYlgoKejYHtFyCN4FNgYUJ31U.woff2) format("woff2");
                unicode-range: u+0460-052f,u+1c80-1c88,u+20b4,u+2de0-2dff,u+a640-a69f,u+fe2e-fe2f
            }

            @font-face {
                font-display: swap;
                font-family: Ubuntu;
                font-style: italic;
                font-weight: 500;
                src: url(https://fonts.gstatic.com/s/ubuntu/v20/4iCp6KVjbNBYlgoKejYHtFyLN4FNgYUJ31U.woff2) format("woff2");
                unicode-range: u+0301,u+0400-045f,u+0490-0491,u+04b0-04b1,u+2116
            }

            @font-face {
                font-display: swap;
                font-family: Ubuntu;
                font-style: italic;
                font-weight: 500;
                src: url(https://fonts.gstatic.com/s/ubuntu/v20/4iCp6KVjbNBYlgoKejYHtFyDN4FNgYUJ31U.woff2) format("woff2");
                unicode-range: u+1f??
            }

            @font-face {
                font-display: swap;
                font-family: Ubuntu;
                font-style: italic;
                font-weight: 500;
                src: url(https://fonts.gstatic.com/s/ubuntu/v20/4iCp6KVjbNBYlgoKejYHtFyMN4FNgYUJ31U.woff2) format("woff2");
                unicode-range: u+0370-0377,u+037a-037f,u+0384-038a,u+038c,u+038e-03a1,u+03a3-03ff
            }

            @font-face {
                font-display: swap;
                font-family: Ubuntu;
                font-style: italic;
                font-weight: 500;
                src: url(https://fonts.gstatic.com/s/ubuntu/v20/4iCp6KVjbNBYlgoKejYHtFyBN4FNgYUJ31U.woff2) format("woff2");
                unicode-range: u+0100-02af,u+0304,u+0308,u+0329,u+1e00-1e9f,u+1ef2-1eff,u+2020,u+20a0-20ab,u+20ad-20c0,u+2113,u+2c60-2c7f,u+a720-a7ff
            }

            @font-face {
                font-display: swap;
                font-family: Ubuntu;
                font-style: italic;
                font-weight: 500;
                src: url(https://fonts.gstatic.com/s/ubuntu/v20/4iCp6KVjbNBYlgoKejYHtFyPN4FNgYUJ.woff2) format("woff2");
                unicode-range: u+00??,u+0131,u+0152-0153,u+02bb-02bc,u+02c6,u+02da,u+02dc,u+0304,u+0308,u+0329,u+2000-206f,u+2074,u+20ac,u+2122,u+2191,u+2193,u+2212,u+2215,u+feff,u+fffd
            }

            @font-face {
                font-display: swap;
                font-family: Ubuntu;
                font-style: italic;
                font-weight: 700;
                src: url(https://fonts.gstatic.com/s/ubuntu/v15/4iCp6KVjbNBYlgoKejZPslyCN4FNgYUJ31U.woff2) format("woff2");
                unicode-range: u+0460-052f,u+1c80-1c88,u+20b4,u+2de0-2dff,u+a640-a69f,u+fe2e-fe2f
            }

            @font-face {
                font-display: swap;
                font-family: Ubuntu;
                font-style: italic;
                font-weight: 700;
                src: url(https://fonts.gstatic.com/s/ubuntu/v15/4iCp6KVjbNBYlgoKejZPslyLN4FNgYUJ31U.woff2) format("woff2");
                unicode-range: u+0400-045f,u+0490-0491,u+04b0-04b1,u+2116
            }

            @font-face {
                font-display: swap;
                font-family: Ubuntu;
                font-style: italic;
                font-weight: 700;
                src: url(https://fonts.gstatic.com/s/ubuntu/v15/4iCp6KVjbNBYlgoKejZPslyDN4FNgYUJ31U.woff2) format("woff2");
                unicode-range: u+1f??
            }

            @font-face {
                font-display: swap;
                font-family: Ubuntu;
                font-style: italic;
                font-weight: 700;
                src: url(https://fonts.gstatic.com/s/ubuntu/v15/4iCp6KVjbNBYlgoKejZPslyMN4FNgYUJ31U.woff2) format("woff2");
                unicode-range: u+0370-03ff
            }

            @font-face {
                font-display: swap;
                font-family: Ubuntu;
                font-style: italic;
                font-weight: 700;
                src: url(https://fonts.gstatic.com/s/ubuntu/v15/4iCp6KVjbNBYlgoKejZPslyBN4FNgYUJ31U.woff2) format("woff2");
                unicode-range: u+0100-024f,u+0259,u+1e??,u+2020,u+20a0-20ab,u+20ad-20cf,u+2113,u+2c60-2c7f,u+a720-a7ff
            }

            @font-face {
                font-display: swap;
                font-family: Ubuntu;
                font-style: italic;
                font-weight: 700;
                src: url(https://fonts.gstatic.com/s/ubuntu/v15/4iCp6KVjbNBYlgoKejZPslyPN4FNgYUJ.woff2) format("woff2");
                unicode-range: u+00??,u+0131,u+0152-0153,u+02bb-02bc,u+02c6,u+02da,u+02dc,u+2000-206f,u+2074,u+20ac,u+2122,u+2191,u+2193,u+2212,u+2215,u+feff,u+fffd
            }

            @font-face {
                font-display: swap;
                font-family: Ubuntu;
                font-style: normal;
                font-weight: 300;
                src: url(https://fonts.gstatic.com/s/ubuntu/v15/4iCv6KVjbNBYlgoC1CzjvWyNPYZvg7UI.woff2) format("woff2");
                unicode-range: u+0460-052f,u+1c80-1c88,u+20b4,u+2de0-2dff,u+a640-a69f,u+fe2e-fe2f
            }

            @font-face {
                font-display: swap;
                font-family: Ubuntu;
                font-style: normal;
                font-weight: 300;
                src: url(https://fonts.gstatic.com/s/ubuntu/v15/4iCv6KVjbNBYlgoC1CzjtGyNPYZvg7UI.woff2) format("woff2");
                unicode-range: u+0400-045f,u+0490-0491,u+04b0-04b1,u+2116
            }

            @font-face {
                font-display: swap;
                font-family: Ubuntu;
                font-style: normal;
                font-weight: 300;
                src: url(https://fonts.gstatic.com/s/ubuntu/v15/4iCv6KVjbNBYlgoC1CzjvGyNPYZvg7UI.woff2) format("woff2");
                unicode-range: u+1f??
            }

            @font-face {
                font-display: swap;
                font-family: Ubuntu;
                font-style: normal;
                font-weight: 300;
                src: url(https://fonts.gstatic.com/s/ubuntu/v15/4iCv6KVjbNBYlgoC1Czjs2yNPYZvg7UI.woff2) format("woff2");
                unicode-range: u+0370-03ff
            }

            @font-face {
                font-display: swap;
                font-family: Ubuntu;
                font-style: normal;
                font-weight: 300;
                src: url(https://fonts.gstatic.com/s/ubuntu/v15/4iCv6KVjbNBYlgoC1CzjvmyNPYZvg7UI.woff2) format("woff2");
                unicode-range: u+0100-024f,u+0259,u+1e??,u+2020,u+20a0-20ab,u+20ad-20cf,u+2113,u+2c60-2c7f,u+a720-a7ff
            }

            @font-face {
                font-display: swap;
                font-family: Ubuntu;
                font-style: normal;
                font-weight: 300;
                src: url(https://fonts.gstatic.com/s/ubuntu/v15/4iCv6KVjbNBYlgoC1CzjsGyNPYZvgw.woff2) format("woff2");
                unicode-range: u+00??,u+0131,u+0152-0153,u+02bb-02bc,u+02c6,u+02da,u+02dc,u+2000-206f,u+2074,u+20ac,u+2122,u+2191,u+2193,u+2212,u+2215,u+feff,u+fffd
            }

            @font-face {
                font-display: swap;
                font-family: Ubuntu;
                font-style: normal;
                font-weight: 400;
                src: url(https://fonts.gstatic.com/s/ubuntu/v15/4iCs6KVjbNBYlgoKcg72nU6AF7xm.woff2) format("woff2");
                unicode-range: u+0460-052f,u+1c80-1c88,u+20b4,u+2de0-2dff,u+a640-a69f,u+fe2e-fe2f
            }

            @font-face {
                font-display: swap;
                font-family: Ubuntu;
                font-style: normal;
                font-weight: 400;
                src: url(https://fonts.gstatic.com/s/ubuntu/v15/4iCs6KVjbNBYlgoKew72nU6AF7xm.woff2) format("woff2");
                unicode-range: u+0400-045f,u+0490-0491,u+04b0-04b1,u+2116
            }

            @font-face {
                font-display: swap;
                font-family: Ubuntu;
                font-style: normal;
                font-weight: 400;
                src: url(https://fonts.gstatic.com/s/ubuntu/v15/4iCs6KVjbNBYlgoKcw72nU6AF7xm.woff2) format("woff2");
                unicode-range: u+1f??
            }

            @font-face {
                font-display: swap;
                font-family: Ubuntu;
                font-style: normal;
                font-weight: 400;
                src: url(https://fonts.gstatic.com/s/ubuntu/v15/4iCs6KVjbNBYlgoKfA72nU6AF7xm.woff2) format("woff2");
                unicode-range: u+0370-03ff
            }

            @font-face {
                font-display: swap;
                font-family: Ubuntu;
                font-style: normal;
                font-weight: 400;
                src: url(https://fonts.gstatic.com/s/ubuntu/v15/4iCs6KVjbNBYlgoKcQ72nU6AF7xm.woff2) format("woff2");
                unicode-range: u+0100-024f,u+0259,u+1e??,u+2020,u+20a0-20ab,u+20ad-20cf,u+2113,u+2c60-2c7f,u+a720-a7ff
            }

            @font-face {
                font-display: swap;
                font-family: Ubuntu;
                font-style: normal;
                font-weight: 400;
                src: url(https://fonts.gstatic.com/s/ubuntu/v15/4iCs6KVjbNBYlgoKfw72nU6AFw.woff2) format("woff2");
                unicode-range: u+00??,u+0131,u+0152-0153,u+02bb-02bc,u+02c6,u+02da,u+02dc,u+2000-206f,u+2074,u+20ac,u+2122,u+2191,u+2193,u+2212,u+2215,u+feff,u+fffd
            }

            @font-face {
                font-display: swap;
                font-family: Ubuntu;
                font-style: normal;
                font-weight: 500;
                src: url(https://fonts.gstatic.com/s/ubuntu/v20/4iCv6KVjbNBYlgoCjC3jvWyNPYZvg7UI.woff2) format("woff2");
                unicode-range: u+0460-052f,u+1c80-1c88,u+20b4,u+2de0-2dff,u+a640-a69f,u+fe2e-fe2f
            }

            @font-face {
                font-display: swap;
                font-family: Ubuntu;
                font-style: normal;
                font-weight: 500;
                src: url(https://fonts.gstatic.com/s/ubuntu/v20/4iCv6KVjbNBYlgoCjC3jtGyNPYZvg7UI.woff2) format("woff2");
                unicode-range: u+0301,u+0400-045f,u+0490-0491,u+04b0-04b1,u+2116
            }

            @font-face {
                font-display: swap;
                font-family: Ubuntu;
                font-style: normal;
                font-weight: 500;
                src: url(https://fonts.gstatic.com/s/ubuntu/v20/4iCv6KVjbNBYlgoCjC3jvGyNPYZvg7UI.woff2) format("woff2");
                unicode-range: u+1f??
            }

            @font-face {
                font-display: swap;
                font-family: Ubuntu;
                font-style: normal;
                font-weight: 500;
                src: url(https://fonts.gstatic.com/s/ubuntu/v20/4iCv6KVjbNBYlgoCjC3js2yNPYZvg7UI.woff2) format("woff2");
                unicode-range: u+0370-0377,u+037a-037f,u+0384-038a,u+038c,u+038e-03a1,u+03a3-03ff
            }

            @font-face {
                font-display: swap;
                font-family: Ubuntu;
                font-style: normal;
                font-weight: 500;
                src: url(https://fonts.gstatic.com/s/ubuntu/v20/4iCv6KVjbNBYlgoCjC3jvmyNPYZvg7UI.woff2) format("woff2");
                unicode-range: u+0100-02af,u+0304,u+0308,u+0329,u+1e00-1e9f,u+1ef2-1eff,u+2020,u+20a0-20ab,u+20ad-20c0,u+2113,u+2c60-2c7f,u+a720-a7ff
            }

            @font-face {
                font-display: swap;
                font-family: Ubuntu;
                font-style: normal;
                font-weight: 500;
                src: url(https://fonts.gstatic.com/s/ubuntu/v20/4iCv6KVjbNBYlgoCjC3jsGyNPYZvgw.woff2) format("woff2");
                unicode-range: u+00??,u+0131,u+0152-0153,u+02bb-02bc,u+02c6,u+02da,u+02dc,u+0304,u+0308,u+0329,u+2000-206f,u+2074,u+20ac,u+2122,u+2191,u+2193,u+2212,u+2215,u+feff,u+fffd
            }

            @font-face {
                font-display: swap;
                font-family: Ubuntu;
                font-style: normal;
                font-weight: 700;
                src: url(https://fonts.gstatic.com/s/ubuntu/v15/4iCv6KVjbNBYlgoCxCvjvWyNPYZvg7UI.woff2) format("woff2");
                unicode-range: u+0460-052f,u+1c80-1c88,u+20b4,u+2de0-2dff,u+a640-a69f,u+fe2e-fe2f
            }

            @font-face {
                font-display: swap;
                font-family: Ubuntu;
                font-style: normal;
                font-weight: 700;
                src: url(https://fonts.gstatic.com/s/ubuntu/v15/4iCv6KVjbNBYlgoCxCvjtGyNPYZvg7UI.woff2) format("woff2");
                unicode-range: u+0400-045f,u+0490-0491,u+04b0-04b1,u+2116
            }

            @font-face {
                font-display: swap;
                font-family: Ubuntu;
                font-style: normal;
                font-weight: 700;
                src: url(https://fonts.gstatic.com/s/ubuntu/v15/4iCv6KVjbNBYlgoCxCvjvGyNPYZvg7UI.woff2) format("woff2");
                unicode-range: u+1f??
            }

            @font-face {
                font-display: swap;
                font-family: Ubuntu;
                font-style: normal;
                font-weight: 700;
                src: url(https://fonts.gstatic.com/s/ubuntu/v15/4iCv6KVjbNBYlgoCxCvjs2yNPYZvg7UI.woff2) format("woff2");
                unicode-range: u+0370-03ff
            }

            @font-face {
                font-display: swap;
                font-family: Ubuntu;
                font-style: normal;
                font-weight: 700;
                src: url(https://fonts.gstatic.com/s/ubuntu/v15/4iCv6KVjbNBYlgoCxCvjvmyNPYZvg7UI.woff2) format("woff2");
                unicode-range: u+0100-024f,u+0259,u+1e??,u+2020,u+20a0-20ab,u+20ad-20cf,u+2113,u+2c60-2c7f,u+a720-a7ff
            }

            @font-face {
                font-display: swap;
                font-family: Ubuntu;
                font-style: normal;
                font-weight: 700;
                src: url(https://fonts.gstatic.com/s/ubuntu/v15/4iCv6KVjbNBYlgoCxCvjsGyNPYZvgw.woff2) format("woff2");
                unicode-range: u+00??,u+0131,u+0152-0153,u+02bb-02bc,u+02c6,u+02da,u+02dc,u+2000-206f,u+2074,u+20ac,u+2122,u+2191,u+2193,u+2212,u+2215,u+feff,u+fffd
            }

            body.dark-mode-toggle,body.dark-mode-toggle :not(.mathquill-rendered-math) {
                transition: color .1s ease-in-out,background-color .1s ease-in-out,border-color .1s ease-in-out
            }

            body {
                background-color: var(--main-bg-color-2);
                font-family: Ubuntu,sans-serif;
                margin: 0;
                padding: 0;
                --main-bg-color-1: #fff;
                --main-bg-color-2: #f6f4f4;
                --main-color-1: #000;
                --main-color-2: #001a36;
                --main-color-3: #cacaca;
                --main-color-4: #9296ac;
                --main-color-5: #7a8795;
                --main-color-6: #234f4f;
                --main-color-7: #4f4f4f;
                --main-border-color-1: #000;
                --main-border-color-2: #eee;
                --main-border-color-3: #cacaca;
                --main-border-color-4: #ddd;
                --sidebar-bg-color: #e3e3e3;
                --sidebar-bg-border-color: #b9b5b5;
                --sidebar-item-border-color: #d9d9d9;
                --sidebar-color: #424242
            }

            body.dark {
                --main-bg-color-1: #000;
                --main-bg-color-2: #090b0b;
                --main-color-1: #fff;
                --main-color-2: #ffe5c9;
                --main-color-3: #353535;
                --main-color-4: #99978a;
                --main-color-5: #6d6458;
                --main-color-6: #fff;
                --main-color-7: #b0b0b0;
                --main-border-color-1: #fff;
                --main-border-color-2: #222;
                --main-border-color-3: #cacaca;
                --main-border-color-4: #222;
                --sidebar-bg-color: #1c1c1c;
                --sidebar-bg-border-color: #464a4a;
                --sidebar-item-border-color: #262626;
                --sidebar-color: #bdbdbd
            }
        </style>
        <style>
            .mobile.header-footer-layout[data-v-bff09cfc] {
                min-width: 350px
            }
        </style>
        <style>
            .logo-container[data-v-d2bca703] {
                cursor: pointer
            }

            header {
                &[data-v-d2bca703] {
                    align-items: center;
                    background-color: #db3f59;
                    box-sizing: border-box;
                    display: flex;
                    gap: 15px;
                    height: 72px;
                    min-width: 1100px;
                    padding: 0 24px 0 15px;
                    position: sticky;
                    top: 0;
                    z-index: 100000
                }

                &.mobile[data-v-d2bca703] {
                    justify-content: space-between;
                    min-width: auto
                }

                .left-side {
                    &[data-v-d2bca703] {
                        align-items: center;
                        display: flex;
                        flex-grow: 1
                    }

                    a[data-v-d2bca703]: first-child {
                        margin-right:17px
                    }
                }

                .logo[data-v-d2bca703] {
                    color: #fff;
                    height: 39px;
                    width: 113px
                }

                .header-icon[data-v-d2bca703] {
                    color: #fff;
                    height: 22px;
                    width: 22px
                }

                .right-side {
                    &[data-v-d2bca703] {
                        align-items: center;
                        display: flex;
                        gap: 18px;
                        height: 72px;
                        margin: 0;
                        padding: 0
                    }

                    .upgrade-button[data-v-d2bca703] {
                        align-items: center;
                        background: #ffc200;
                        border: none;
                        border-radius: 20px;
                        color: #fff;
                        cursor: pointer;
                        display: flex;
                        flex-direction: row;
                        font-size: 10pt;
                        font-weight: 700;
                        height: unset!important;
                        justify-content: center;
                        padding: 10px;
                        text-decoration: none;
                        width: unset!important
                    }
                }
            }
        </style>
        <style>
            .nuxt-icon {
                height: 1em;
                margin-bottom: .125em;
                vertical-align: middle;
                width: 1em
            }

            .nuxt-icon--fill,.nuxt-icon--fill * {
                fill: currentColor
            }
        </style>
        <style>
            .header-nav {
                &[data-v-6bd0ef5c] {
                    position: relative;
                    white-space: nowrap
                }

                .tools-menu[data-v-6bd0ef5c] {
                    display: none
                }

                &:hover .tools-menu[data-v-6bd0ef5c] {
                    display: block
                }

                .header-icon[data-v-6bd0ef5c] {
                    color: #fff;
                    height: 22px;
                    width: 22px
                }

                &:hover .header-icon[data-v-6bd0ef5c] {
                    color: #a92232
                }

                &:hover {
                    span[data-v-6bd0ef5c] {
                        color: #a92232
                    }
                }

                a {
                    &[data-v-6bd0ef5c] {
                        align-items: center;
                        display: flex;
                        flex-direction: column;
                        gap: 6px;
                        height: 80px;
                        justify-content: center;
                        text-decoration: none;
                        width: 80px
                    }

                    span[data-v-6bd0ef5c] {
                        color: #fff;
                        font-size: .65rem;
                        font-weight: 500;
                        text-align: center;
                        text-decoration: none
                    }
                }
            }
        </style>
        <style>
            body .tools-menu[data-v-40e089d6] {
                --menu-hover-bg-color-1: #db3f5921
            }

            body.dark .tools-menu[data-v-40e089d6] {
                --menu-hover-bg-color-1: rgba(239,88,88,.25)
            }

            .tools-menu {
                &[data-v-40e089d6] {
                    background-color: var(--main-bg-color-1);
                    border-radius: 8px;
                    box-shadow: 0 1.744px 13.95px 0 rgba(0,0,0,.1);
                    cursor: pointer;
                    display: flex;
                    flex-direction: column;
                    left: 0;
                    overflow: clip;
                    position: absolute;
                    top: 76px;
                    vertical-align: middle
                }

                a {
                    &[data-v-40e089d6] {
                        align-items: center;
                        display: flex;
                        flex-direction: row;
                        gap: 8px;
                        line-height: 36px;
                        padding: 0 16px;
                        text-decoration: none
                    }

                    &[data-v-40e089d6]: not(:last-child) {
                        border-bottom:1px solid var(--main-border-color-2)
                    }

                    &[data-v-40e089d6]: hover {
                        background-color:var(--menu-hover-bg-color-1)
                    }

                    span[data-v-40e089d6] {
                        font-size: .787rem;
                        font-weight: 400
                    }

                    .tools-menu-icon[data-v-40e089d6],span[data-v-40e089d6] {
                        color: var(--main-color-2)
                    }

                    .tools-menu-icon[data-v-40e089d6] {
                        height: 22px;
                        width: 22px
                    }
                }
            }
        </style>
        <style>
            .store-logo[data-v-838b28d2] {
                background-color: transparent;
                border: 0;
                display: inline;
                padding: 0
            }
        </style>
        <style>
            .header-search {
                &[data-v-28b74b68] {
                    background-color: #c53950;
                    border-radius: 50px;
                    height: 48px;
                    position: relative;
                    transition: width .2s ease-in-out;
                    width: 48px
                }

                .search-container {
                    &[data-v-28b74b68] {
                        align-items: center;
                        box-sizing: border-box;
                        cursor: pointer;
                        display: flex;
                        flex-direction: row;
                        height: 100%;
                        justify-content: center;
                        padding: 0 10px;
                        width: 100%
                    }

                    svg[data-v-28b74b68] {
                        height: 22px;
                        width: 22px;
                        stroke-width: 2;
                        stroke: #fff;
                        fill: transparent;
                        flex-shrink: 0
                    }

                    input[data-v-28b74b68] {
                        background-color: transparent;
                        border: none;
                        color: #fff;
                        flex-grow: 1;
                        font-size: 14px;
                        max-width: 0;
                        outline: none;
                        padding: 0;
                        transition-duration: .2s;
                        transition-property: width,max-width,margin-left;
                        transition-timing-function: ease-in-out;
                        width: 0
                    }
                }

                &.open {
                    &[data-v-28b74b68] {
                        width: 180px
                    }

                    input[data-v-28b74b68] {
                        margin-left: 10px;
                        max-width: 128px;
                        width: 128px
                    }
                }

                .dropdown {
                    &[data-v-28b74b68] {
                        background-color: #fff;
                        border: 1px solid #d2d0d0;
                        font-family: Ubuntu,sans-serif;
                        font-size: 11px;
                        opacity: 1;
                        padding: 10px;
                        transition: opacity .25s,display .25s;
                        transition-behavior: allow-discrete
                    }

                    @starting-style {
                        &[data-v-28b74b68] {
                            opacity: 0
                        }
                    }

                    .heading[data-v-28b74b68] {
                        font-weight: 700;
                        margin-top: 10px
                    }

                    .item {
                        &[data-v-28b74b68] {
                            color: #000;
                            cursor: pointer;
                            display: block;
                            text-decoration: none
                        }

                        &[data-v-28b74b68]: hover {
                            background-color:#db3f5921
                        }

                        div[data-v-28b74b68] {
                            padding: 3px 15px
                        }
                    }
                }
            }

            input[data-v-28b74b68]::-moz-placeholder {
                color: #d59898
            }

            input[data-v-28b74b68]::placeholder {
                color: #d59898
            }
        </style>
        <style>
            body .header-language[data-v-39804e6d] {
                --menu-hover-bg-color-1: #db3f5921
            }

            body.dark .header-language[data-v-39804e6d] {
                --menu-hover-bg-color-1: rgba(239,88,88,.25)
            }

            .header-language {
                &[data-v-39804e6d] {
                    color: #fff;
                    cursor: pointer;
                    font-size: 12pt;
                    font-weight: 700;
                    line-height: 80px;
                    position: relative;
                    text-transform: uppercase;
                    vertical-align: middle
                }

                &:hover .language-selector[data-v-39804e6d] {
                    display: flex
                }

                .language-selector {
                    &[data-v-39804e6d] {
                        background: var(--main-bg-color-1);
                        border-radius: 8px;
                        box-shadow: 0 1px 20px rgba(0,0,0,.05);
                        display: none;
                        flex-direction: column;
                        left: 0;
                        min-width: 180px;
                        overflow: hidden;
                        position: absolute;
                        top: 65px;
                        z-index: 20
                    }

                    div {
                        &[data-v-39804e6d] {
                            border-bottom: 1px solid var(--main-border-color-2);
                            color: var(--main-color-2);
                            cursor: pointer;
                            display: block;
                            font-size: 9pt;
                            font-weight: 400;
                            line-height: 40px;
                            padding: 2px 16px;
                            position: relative;
                            text-decoration: none;
                            text-transform: none;
                            white-space: nowrap
                        }

                        &.selected[data-v-39804e6d]: after {
                            color:var(--main-color-4);
                            content: "✔";
                            position: absolute;
                            right: 20px
                        }

                        &[data-v-39804e6d]: hover {
                            background-color:var(--menu-hover-bg-color-1);
                            color: var(--main-color-1)
                        }
                    }
                }
            }
        </style>
        <style>
            .header-color-scheme {
                svg[data-v-1bc384b9] {
                    height: 16px;
                    width: 16px;
                    fill: #fff
                }
            }
        </style>
        <style>
            .header-avatar {
                &[data-v-d3dc2a2c] {
                    align-items: center;
                    display: flex;
                    flex-direction: row;
                    height: 100%;
                    position: relative
                }

                .avatar-button {
                    &[data-v-d3dc2a2c] {
                        background-color: #f4f3f3;
                        border: none;
                        border-radius: 24px;
                        cursor: pointer;
                        height: 42px;
                        line-height: 0;
                        margin: 0;
                        padding: 0;
                        position: relative;
                        width: 42px
                    }

                    .signing-in-progress[data-v-d3dc2a2c] {
                        animation: rotating-d3dc2a2c 1.2s linear infinite;
                        border: 3px dashed #d23d57;
                        border-radius: 50%;
                        box-sizing: border-box;
                        inset: 0;
                        position: absolute
                    }

                    .upgrade-badge-container {
                        &[data-v-d3dc2a2c] {
                            bottom: -6px;
                            display: flex;
                            justify-content: center;
                            position: absolute;
                            white-space: pre;
                            width: 100%
                        }

                        span[data-v-d3dc2a2c] {
                            background-color: #ffc200;
                            border-radius: 2px;
                            color: #fff;
                            font-size: 7px;
                            font-weight: 700;
                            height: 12px;
                            line-height: 12px;
                            padding: 0 4px;
                            text-align: center
                        }
                    }

                    img[data-v-d3dc2a2c] {
                        border-radius: 80px;
                        display: inline-block;
                        height: 43px;
                        vertical-align: middle;
                        width: 43px
                    }

                    svg[data-v-d3dc2a2c] {
                        filter: grayscale(1);
                        height: 36px;
                        width: 36px;
                        fill: none
                    }

                    &.signed-in svg[data-v-d3dc2a2c] {
                        filter: none
                    }
                }

                &:hover .avatar-options[data-v-d3dc2a2c] {
                    display: flex
                }

                .avatar-options {
                    &[data-v-d3dc2a2c] {
                        background: #fff;
                        border-radius: 8px;
                        box-shadow: 0 1px 20px rgba(0,0,0,.05);
                        display: none;
                        flex-direction: column;
                        left: -138px;
                        min-width: 180px;
                        overflow: hidden;
                        position: absolute;
                        top: 61px;
                        z-index: 20
                    }

                    a {
                        &[data-v-d3dc2a2c] {
                            border-bottom: 1px solid #eee;
                            color: #001a36;
                            cursor: pointer;
                            display: block;
                            font-size: 9pt;
                            font-weight: 400;
                            line-height: 40px;
                            padding: 2px 16px;
                            text-decoration: none;
                            text-transform: none;
                            white-space: nowrap
                        }

                        &[data-v-d3dc2a2c]: hover {
                            background-color:#db3f5921;
                            color: #000
                        }
                    }
                }
            }

            @keyframes rotating-d3dc2a2c {
                to {
                    transform: rotate(1turn)
                }
            }
        </style>
        <style>
            body .popular-view[data-v-38a56602] {
                --box-title-color: #234f4f
            }

            body.dark .popular-view[data-v-38a56602] {
                --box-title-color: #dcb0b0
            }

            .popular-view {
                .breadcrumbs {
                    &[data-v-38a56602] {
                        background-color: var(--main-bg-color-2);
                        color: #7a8795;
                        font-size: 11pt;
                        height: 50px;
                        min-width: 1100px
                    }

                    .breadcrumbs-content[data-v-38a56602] {
                        margin: 0 auto;
                        max-width: 1100px;
                        overflow: hidden;
                        text-overflow: ellipsis;
                        white-space: nowrap
                    }

                    h1[data-v-38a56602] {
                        display: inline;
                        font-size: 15pt;
                        line-height: 50px
                    }

                    h1[data-v-38a56602],span[data-v-38a56602]: first-child {
                        font-weight:700
                    }
                }

                .main-content[data-v-38a56602] {
                    display: flex;
                    flex-direction: row;
                    gap: 20px;
                    margin: 0 auto;
                    max-width: 1200px
                }

                &.mobile {
                    .breadcrumbs-content[data-v-38a56602],.main-content[data-v-38a56602] {
                        padding: 0 15px
                    }

                    .main-content[data-v-38a56602] {
                        width: auto
                    }
                }

                .popular-container {
                    &[data-v-38a56602] {
                        flex-grow: 1;
                        min-width: 780px;
                        padding-bottom: 60px;
                        width: 100%
                    }

                    .box-title[data-v-38a56602] {
                        color: var(--box-title-color);
                        font-family: Ubuntu,sans-serif;
                        font-size: 16px;
                        font-style: normal;
                        font-weight: 300;
                        margin-top: 20px
                    }

                    .solution-container[data-v-38a56602] {
                        border-radius: 8px
                    }

                    .advanced-calculator {
                        &[data-v-38a56602] {
                            margin: 30px auto 0
                        }

                        button[data-v-38a56602] {
                            align-items: center;
                            background-color: #041a93;
                            border: none;
                            border-radius: 360px;
                            color: #fff;
                            cursor: pointer;
                            display: flex;
                            font-family: Ubuntu,sans-serif;
                            font-size: 11.5pt;
                            font-weight: 700;
                            gap: 16px;
                            height: 44px;
                            margin: 0 auto 30px;
                            padding: 0 24px;
                            position: relative
                        }

                        svg[data-v-38a56602] {
                            height: 20px;
                            width: 20px
                        }
                    }
                }

                .ads[data-v-38a56602] {
                    flex-shrink: 0;
                    width: 320px
                }

                &.mobile {
                    .breadcrumbs[data-v-38a56602],.popular-container[data-v-38a56602] {
                        min-width: auto
                    }
                }
            }

            @keyframes blinker-38a56602 {
                to {
                    rotate: 1turn
                }
            }
        </style>
        <style>
            body .footer[data-v-b3dea1e9] {
                --social-bg-color: #f3f3f3
            }

            body.dark .footer[data-v-b3dea1e9] {
                --social-bg-color: #202020
            }

            .footer {
                &[data-v-b3dea1e9] {
                    background-color: var(--main-bg-color-1);
                    box-sizing: border-box;
                    clear: both;
                    min-width: 1100px;
                    padding: 50px 24px 24px;
                    width: 100%
                }

                &.desktop #footer-top[data-v-b3dea1e9] {
                    position: relative
                }

                nav {
                    &[data-v-b3dea1e9] {
                        display: flex;
                        flex-direction: row;
                        gap: 55px;
                        justify-content: center;
                        padding: 0;
                        width: 100%
                    }

                    .home-only {
                        &[data-v-b3dea1e9] {
                            flex-grow: 0
                        }

                        svg {
                            &[data-v-b3dea1e9] {
                                cursor: pointer;
                                height: 67px;
                                width: 182px
                            }

                            &[data-v-b3dea1e9] path {
                                fill: #db3f59
                            }
                        }
                    }

                    .footer-links {
                        &[data-v-b3dea1e9] {
                            display: grid;
                            gap: 55px;
                            grid-template-columns: repeat(4,auto)
                        }

                        .footer-links-section[data-v-b3dea1e9] {
                            align-items: flex-start;
                            display: flex;
                            flex-direction: column;
                            gap: 24px
                        }
                    }

                    div span.footer-title[data-v-b3dea1e9] {
                        color: #7a8795;
                        display: block;
                        font-weight: 700;
                        text-transform: uppercase
                    }

                    .social-media-panel {
                        &[data-v-b3dea1e9] {
                            align-items: flex-end;
                            display: flex;
                            flex-direction: column;
                            gap: 24px
                        }

                        #social-buttons {
                            &[data-v-b3dea1e9] {
                                display: flex;
                                flex-direction: row;
                                gap: 8px
                            }

                            a[data-v-b3dea1e9] {
                                align-items: center;
                                background: var(--social-bg-color);
                                border-radius: 8px;
                                display: flex;
                                height: 50px;
                                justify-content: center;
                                width: 50px
                            }

                            svg[data-v-b3dea1e9] {
                                height: 22px;
                                width: 22px
                            }
                        }

                        .social-title[data-v-b3dea1e9] {
                            margin-top: 130px
                        }
                    }

                    .feedback-button {
                        &[data-v-b3dea1e9] {
                            align-items: center;
                            background: #db3f59;
                            border: none;
                            border-radius: 8px;
                            color: #fff;
                            cursor: pointer;
                            display: flex;
                            flex-direction: row;
                            gap: 8px;
                            outline: none;
                            padding: 16px 24px
                        }

                        svg[data-v-b3dea1e9] {
                            height: 24px;
                            width: 24px
                        }
                    }

                    a[data-v-b3dea1e9],button[data-v-b3dea1e9],span.span-footer-link[data-v-b3dea1e9] {
                        color: #7a8795;
                        cursor: pointer;
                        text-decoration: none
                    }

                    button[data-v-b3dea1e9] {
                        background-color: transparent;
                        border: none;
                        font-family: Ubuntu,sans-serif;
                        outline: none;
                        padding: 0
                    }
                }

                #footer-bottom[data-v-b3dea1e9] {
                    color: #7a8795;
                    font-size: 10pt;
                    margin-left: 64px;
                    padding-bottom: 32px
                }

                div span.footer-title[data-v-b3dea1e9] {
                    max-width: 200px
                }

                &.desktop {
                    nav {
                        a[data-v-b3dea1e9],span[data-v-b3dea1e9] {
                            font-size: 10pt
                        }
                    }
                }

                &.mobile {
                    &[data-v-b3dea1e9] {
                        min-width: auto;
                        padding: 24px
                    }

                    nav {
                        &[data-v-b3dea1e9] {
                            flex-direction: column;
                            padding: 0
                        }

                        a[data-v-b3dea1e9],button[data-v-b3dea1e9],span[data-v-b3dea1e9] {
                            font-size: 12pt
                        }

                        .footer-links[data-v-b3dea1e9] {
                            @media screen and (max-width: 768px) {
                                grid-template-columns:repeat(2,auto)
                            }
                        }

                        .social-media-panel[data-v-b3dea1e9] {
                            display: none
                        }

                        .home-only svg[data-v-b3dea1e9] {
                            height: 32px;
                            width: 106px
                        }
                    }
                }

                #footer-bottom[data-v-b3dea1e9] {
                    margin-top: 10px
                }

                &.mobile #footer-bottom[data-v-b3dea1e9] {
                    margin: 24px 0 0;
                    text-align: center
                }

                #separator[data-v-b3dea1e9] {
                    background-color: var(--main-border-color-2);
                    border: 0;
                    color: var(--main-border-color-2);
                    display: block;
                    height: 1px;
                    margin: 0 24px 32px
                }
            }
        </style>
        <style>
            .nl-leftNav {
                &[data-v-99b8b4c0] {
                    background-color: var(--sidebar-bg-color);
                    border-right: 1px solid var(--sidebar-bg-border-color);
                    flex-shrink: 0;
                    min-height: 900px;
                    padding: 10px;
                    width: 160px
                }

                ul {
                    &[data-v-99b8b4c0] {
                        list-style: none;
                        margin: 0;
                        padding: 0
                    }

                    li {
                        &[data-v-99b8b4c0] {
                            border-bottom: 1px solid var(--sidebar-item-border-color);
                            padding: 16px 0
                        }

                        a[data-v-99b8b4c0] {
                            color: var(--sidebar-color);
                            display: inline-block;
                            font-family: Ubuntu,sans-serif;
                            font-size: 13px;
                            margin-left: 14px;
                            text-decoration: none
                        }
                    }
                }
            }
        </style>
        <style>
            [data-v-a1d9f1fc]::-webkit-scrollbar {
                height: 4px;
                width: 4px
            }

            [data-v-a1d9f1fc]::-webkit-scrollbar-track {
                background: #f1f1f1;
                border-radius: 2px
            }

            [data-v-a1d9f1fc]::-webkit-scrollbar-thumb {
                background: #bec4c4;
                border-radius: 2px
            }

            [data-v-a1d9f1fc]::-webkit-scrollbar-thumb:hover {
                background: #555
            }

            .solution {
                &[data-v-a1d9f1fc] {
                    background-color: var(--main-bg-color-1);
                    border-radius: 8px;
                    padding: 24px
                }

                .query-math {
                    &[data-v-a1d9f1fc] {
                        color: #001a36;
                        font-size: 20px
                    }

                    [data-v-a1d9f1fc] .katex {
                        font-size: 20.24px
                    }
                }

                .solution-math {
                    &[data-v-a1d9f1fc] {
                        color: var(--main-color-2);
                        font-size: 26px;
                        overflow-x: auto;
                        overflow-y: hidden
                    }

                    [data-v-a1d9f1fc] .katex {
                        font-size: 24px
                    }
                }

                .solution-title[data-v-a1d9f1fc] {
                    color: var(--main-color-3);
                    font-size: 13.5pt;
                    font-weight: 400;
                    margin: 0;
                    padding: 25px 0 16px
                }

                .solution-container {
                    &[data-v-a1d9f1fc] {
                        display: flex;
                        flex-direction: row;
                        gap: 10px
                    }

                    .solution-math[data-v-a1d9f1fc] {
                        flex-grow: 1
                    }

                    .format-indicator {
                        &[data-v-a1d9f1fc] {
                            align-items: center;
                            color: #7a8795;
                            cursor: pointer;
                            display: flex;
                            flex-direction: row;
                            font-size: 14px;
                            font-weight: bolder;
                            gap: 5px
                        }

                        svg[data-v-a1d9f1fc] {
                            transform: rotate(180deg)
                        }

                        &.open svg[data-v-a1d9f1fc] {
                            transform: rotate(0deg)
                        }
                    }
                }

                .other-solutions {
                    &[data-v-a1d9f1fc] {
                        color: #7a8795;
                        display: flex;
                        flex-direction: row;
                        gap: 20px;
                        margin-top: 27px;
                        overflow-x: auto;
                        overflow-y: hidden;
                        padding-bottom: 5px
                    }

                    .one-solution {
                        &[data-v-a1d9f1fc] {
                            border: 1px solid #cacaca;
                            border-radius: 8px;
                            flex-shrink: 0;
                            font-size: 26px;
                            padding: 8px 22px
                        }

                        .one-solution-title[data-v-a1d9f1fc] {
                            font-family: Ubuntu,sans-serif;
                            font-size: .75rem;
                            font-weight: 400
                        }

                        [data-v-a1d9f1fc] .katex {
                            font-size: 23px
                        }
                    }

                    &[data-v-a1d9f1fc]: :-webkit-scrollbar {
                        border:1px solid #d5d5d5;
                        height: 4px;
                        width: 2px
                    }

                    &[data-v-a1d9f1fc]: :-webkit-scrollbar-thumb {
                        background:#7a8795;
                        border-radius: 4px
                    }
                }

                .steps-title-container {
                    &[data-v-a1d9f1fc] {
                        align-items: center;
                        display: flex;
                        flex-direction: row;
                        justify-content: space-between;
                        padding-bottom: 30px
                    }

                    .steps-title[data-v-a1d9f1fc] {
                        color: var(--main-color-2);
                        font-size: 15pt;
                        font-weight: 700
                    }
                }
            }
        </style>
        <style>
            .mathquill-text {
                display: inline-block;
                padding-bottom: 6px;
                -webkit-text-size-adjust: 100%;
                white-space: pre;
                &.force-no-scroll {
                    white-space: unset
                }
            }
        </style>
        <style>
            .sy-katex {
                &[data-v-7862221b] {
                    overflow: auto hidden
                }

                &.force-no-scroll {
                    &[data-v-7862221b] {
                        overflow: initial
                    }

                    &[data-v-7862221b] .katex {
                        white-space: normal!important
                    }

                    &[data-v-7862221b] .katex .base {
                        white-space: normal!important;
                        width: auto!important
                    }
                }

                &[data-v-7862221b]: not(.force-no-scroll) * {
                    white-space:pre
                }

                &.own-line[data-v-7862221b] {
                    display: block;
                    padding-bottom: 5px
                }

                &[data-v-7862221b] .katex-display {
                    display: inline-block;
                    margin: 1px 0;
                    text-align: initial!important
                }

                &[data-v-7862221b] .katex-display .katex {
                    display: inline-block;
                    text-align: initial!important
                }

                &[data-v-7862221b] .katex-display .katex .katex-html {
                    display: inline-block
                }
            }
        </style>
        <style>
            .show-hide-container {
                &[data-v-64550a09] {
                    margin: 30px 0;
                    position: relative
                }

                .dashed-line[data-v-64550a09] {
                    background-image: linear-gradient(90deg,#db3f59 60%,hsla(0,0%,100%,0) 0);
                    background-position: 50%;
                    background-repeat: repeat-x;
                    background-size: 12px 2px;
                    height: 20px
                }

                .hide-button[data-v-64550a09] {
                    background-color: var(--main-bg-color-1);
                    border: 1px solid var(--main-border-color-2);
                    color: #db3f59;
                    gap: 10px;
                    left: 50%;
                    padding: 8px 14px;
                    position: absolute;
                    top: 50%;
                    transform: translate(-50%,-50%)
                }

                .hide-button[data-v-64550a09],.show-button[data-v-64550a09] {
                    border-radius: 8px;
                    cursor: pointer;
                    display: flex;
                    font-family: Ubuntu,sans-serif;
                    font-size: 16px
                }

                .show-button[data-v-64550a09] {
                    background-color: #db3f59;
                    border: none;
                    color: #fff;
                    height: 48px;
                    justify-content: center;
                    line-height: 48px;
                    margin: 23px auto 0;
                    -webkit-user-select: none;
                    -moz-user-select: none;
                    user-select: none;
                    vertical-align: middle;
                    width: min(300px,80%)
                }
            }
        </style>
        <style>
            [data-v-01787b30]::-webkit-scrollbar {
                height: 4px;
                width: 4px
            }

            [data-v-01787b30]::-webkit-scrollbar-track {
                background: #f1f1f1;
                border-radius: 2px
            }

            [data-v-01787b30]::-webkit-scrollbar-thumb {
                background: #bec4c4;
                border-radius: 2px
            }

            [data-v-01787b30]::-webkit-scrollbar-thumb:hover {
                background: #555
            }

            .steps-container {
                &[data-v-01787b30] {
                    background-color: var(--main-bg-color-1)
                }

                .input-math {
                    &[data-v-01787b30] {
                        border-bottom: 1px solid var(--main-border-color-2);
                        color: var(--main-color-1);
                        margin-bottom: 20px;
                        padding-bottom: 20px
                    }

                    &[data-v-01787b30] .katex {
                        font-size: 17px
                    }
                }

                .inner-step[data-v-01787b30] {
                    margin-bottom: 18px;
                    margin-top: 18px
                }
            }
        </style>
        <style>
            [data-v-9172ad38]::-webkit-scrollbar {
                height: 4px;
                width: 4px
            }

            [data-v-9172ad38]::-webkit-scrollbar-track {
                background: #f1f1f1;
                border-radius: 2px
            }

            [data-v-9172ad38]::-webkit-scrollbar-thumb {
                background: #bec4c4;
                border-radius: 2px
            }

            [data-v-9172ad38]::-webkit-scrollbar-thumb:hover {
                background: #555
            }

            .regular-step {
                &[data-v-9172ad38] {
                    display: flex;
                    flex-direction: column;
                    padding: 0 13px
                }

                &.upper-level[data-v-9172ad38] {
                    padding: 0
                }

                hr[data-v-9172ad38] {
                    border: none;
                    border-bottom: 1px solid var(--main-border-color-2);
                    width: 100%
                }

                .primary,.secondary {
                    &[data-v-9172ad38] {
                        color: var(--main-color-4);
                        overflow-x: auto;
                        overflow-y: hidden;
                        white-space: pre
                    }

                    &[data-v-9172ad38] .katex {
                        font-size: 1.1em
                    }
                }

                .secondary[data-v-9172ad38] {
                    margin-top: 20px
                }

                .result {
                    &[data-v-9172ad38] {
                        color: var(--main-color-1);
                        margin: 20px 0 0;
                        overflow-x: auto;
                        overflow-y: hidden
                    }

                    &.separator[data-v-9172ad38] {
                        border-bottom: 1px solid var(--main-border-color-2);
                        padding-bottom: 20px
                    }

                    &[data-v-9172ad38] .katex {
                        font-size: 17px
                    }
                }
            }
        </style>
        <style>
            [data-v-336b5e13]::-webkit-scrollbar {
                height: 4px;
                width: 4px
            }

            [data-v-336b5e13]::-webkit-scrollbar-track {
                background: #f1f1f1;
                border-radius: 2px
            }

            [data-v-336b5e13]::-webkit-scrollbar-thumb {
                background: #bec4c4;
                border-radius: 2px
            }

            [data-v-336b5e13]::-webkit-scrollbar-thumb:hover {
                background: #555
            }

            body .interim-step[data-v-336b5e13] {
                --steps-background-1: #edfbff;
                --steps-background-2: #b8f0ff
            }

            body.dark .interim-step[data-v-336b5e13] {
                --steps-background-1: #10272e;
                --steps-background-2: #174b59
            }

            .interim-step {
                &[data-v-336b5e13] {
                    padding: 0 7px
                }

                &.opened[data-v-336b5e13],&.upper-level[data-v-336b5e13] {
                    padding: 0
                }

                &.opened[data-v-336b5e13] {
                    margin: 20px 0
                }

                .interim-step-main {
                    &[data-v-336b5e13] {
                        background-color: var(--steps-background-1);
                        border-radius: 4px 4px 8px 8px
                    }

                    &.opened {
                        &[data-v-336b5e13] {
                            background-color: var(--steps-background-2)
                        }

                        .interim-content {
                            &[data-v-336b5e13] {
                                padding: 0 5px 5px
                            }

                            &.inner-level[data-v-336b5e13] {
                                left: -3px;
                                position: relative;
                                width: calc(100% - 4px)
                            }
                        }
                    }

                    .title {
                        &[data-v-336b5e13] {
                            align-items: center;
                            cursor: pointer;
                            display: flex;
                            gap: 10px;
                            min-height: 33px;
                            padding: 10px 20px
                        }

                        .title-text {
                            &[data-v-336b5e13] {
                                color: var(--main-color-1);
                                flex-grow: 1;
                                overflow-x: auto;
                                overflow-y: hidden;
                                white-space: pre
                            }

                            &[data-v-336b5e13] .katex {
                                font-size: 1.1em
                            }
                        }

                        svg {
                            &[data-v-336b5e13] {
                                color: var(--main-color-1);
                                flex-shrink: 0;
                                height: 10px;
                                transform: scaleY(-1);
                                transition: transform .2s;
                                width: 16px
                            }

                            &.opened[data-v-336b5e13] {
                                transform: scaleY(1)
                            }
                        }
                    }

                    .interim-content {
                        .inner-steps {
                            &[data-v-336b5e13] {
                                background-color: var(--main-bg-color-1);
                                border-radius: 4px;
                                display: flex;
                                flex-direction: column
                            }

                            .inner-step[data-v-336b5e13] {
                                margin-bottom: 8px;
                                margin-top: 8px
                            }

                            .input {
                                &[data-v-336b5e13] {
                                    border-bottom: 1px solid var(--main-border-color-2);
                                    color: var(--main-color-1);
                                    margin-bottom: 18px;
                                    padding: 16px 10px
                                }

                                &[data-v-336b5e13] .katex {
                                    font-size: 17px
                                }
                            }
                        }
                    }
                }

                .result {
                    &[data-v-336b5e13] {
                        color: var(--main-color-1);
                        margin: 20px 10px
                    }

                    &.separator[data-v-336b5e13] {
                        border-bottom: 1px solid var(--main-border-color-2);
                        padding-bottom: 20px
                    }

                    &[data-v-336b5e13] .katex {
                        font-size: 1.1em
                    }
                }
            }
        </style>
        <style>
            body .popular-examples[data-v-953aa121] {
                --example-color: #707070;
                --example-link-color: #3161fd
            }

            body.dark .popular-examples[data-v-953aa121] {
                --example-color: #8f8f8f;
                --example-link-color: #ce9e02
            }

            .popular-examples {
                &[data-v-953aa121] {
                    background-color: var(--main-bg-color-1);
                    border: 1px solid #ccc;
                    border-collapse: collapse;
                    border-radius: 6px;
                    border-spacing: 0;
                    color: var(--example-color);
                    cursor: text;
                    display: grid;
                    font-size: 14px;
                    gap: 10px 20px;
                    grid-template-columns: fit-content(100%) 1fr;
                    line-height: 16px;
                    margin-bottom: 3px;
                    margin-top: 10px;
                    padding: 10px;
                    vertical-align: middle
                }

                a[data-v-953aa121] {
                    align-self: center;
                    color: var(--example-link-color);
                    line-height: 1;
                    text-decoration: none
                }

                a.example[data-v-953aa121] {
                    color: #707070
                }
            }
        </style>
        <style>
            .popular-faqs {
                &[data-v-9c91cd27] {
                    font-size: 12.5px;
                    list-style: none;
                    padding: 0
                }

                li {
                    &[data-v-9c91cd27] {
                        color: var(--main-color-1);
                        margin-top: 30px
                    }

                    h3[data-v-9c91cd27] {
                        font-size: 1.17em;
                        margin: 1em 0
                    }
                }
            }
        </style>
        <style>
            .popular-ads {
                &[data-v-6222bc7d] {
                    height: -moz-fit-content;
                    height: fit-content;
                    margin-bottom: 20px;
                    margin-top: 20px;
                    position: sticky;
                    top: 90px
                }

                .ads-pane[data-v-6222bc7d] {
                    display: flex;
                    flex-direction: column;
                    gap: 20px
                }
            }
        </style>
        <link rel="stylesheet" href="/_nuxt/entry.orWOxeYo.css" crossorigin>
        <link rel="stylesheet" href="/_nuxt/nuxt-icon.Cvbtxq7p.css" crossorigin>
        <link rel="stylesheet" href="/_nuxt/use-google-sign-in.DF7G1mAI.css" crossorigin>
        <link rel="stylesheet" href="/_nuxt/animated-loading-spinner.0cb82txz.css" crossorigin>
        <link rel="preload" href="https://cdn.cookielaw.org/consent/28cd3f47-fef1-4429-be4b-ff2acc7f492b/OtAutoBlock.js" as="script">
        <link rel="preload" href="https://cdn.cookielaw.org/scripttemplates/otSDKStub.js" as="script">
        <link rel="preload" href="https://accounts.google.com/gsi/client" as="script">
        <link rel="modulepreload" as="script" crossorigin href="/_nuxt/KRGuqoqh.js">
        <link rel="modulepreload" as="script" crossorigin href="/_nuxt/_6CIssJA.js">
        <link rel="modulepreload" as="script" crossorigin href="/_nuxt/D_Stzl5v.js">
        <link rel="modulepreload" as="script" crossorigin href="/_nuxt/DlAUqK2U.js">
        <link rel="modulepreload" as="script" crossorigin href="/_nuxt/C3pqMNe5.js">
        <link rel="modulepreload" as="script" crossorigin href="/_nuxt/BrZWyHHf.js">
        <link rel="modulepreload" as="script" crossorigin href="/_nuxt/iSogeznt.js">
        <link rel="modulepreload" as="script" crossorigin href="/_nuxt/DYZaMX3N.js">
        <link rel="modulepreload" as="script" crossorigin href="/_nuxt/B6zWL1Qt.js">
        <link rel="modulepreload" as="script" crossorigin href="/_nuxt/BM1QglUv.js">
        <link rel="prefetch" as="script" crossorigin href="/_nuxt/DoXKkab-.js">
        <link rel="prefetch" as="script" crossorigin href="/_nuxt/BOz9oNPY.js">
        <meta http-equiv="Content-Security-Policy" content="upgrade-insecure-requests; object-src 'none'">
        <link rel="icon" type="image/svg+xml" href="/favicon.svg">
        <link rel="alternate" hreflang="en" href="https://www.symbolab.com/popular-algebra/algebra-106">
        <link rel="canonical" href="https://www.symbolab.com/popular-algebra/algebra-106">
        <link rel="alternate" hreflang="x-default" href="https://www.symbolab.com/popular-algebra/algebra-106">
        <link rel="alternate" hreflang="es" href="https://es.symbolab.com/popular-algebra/algebra-106">
        <script type="application/ld+json">
            {
                "@context": "https://schema.org",
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": 1,
                        "name": "Popular Problems",
                        "item": "https://www.symbolab.com/popular-algebra"
                    },
                    {
                        "@type": "ListItem",
                        "position": 2,
                        "name": "problem",
                        "item": "https://www.symbolab.com/popular-algebra/algebra-106"
                    }
                ]
            }</script>
        <script type="application/ld+json">
            {
                "@context": "https://schema.org",
                "@type": "FAQPage",
                "mainEntity": [
                    {
                        "@type": "Question",
                        "name": "What is 169^{-1/2} ?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "The solution to 169^{-1/2} is 1/13"
                        }
                    }
                ]
            }</script>
        <meta name="description" content="Detailed step by step solution for simplify 169^{-1/2}">
        <meta property="og:title" content="simplify 169^{-1/2}">
        <meta property="og:description" content="Detailed step by step solution for simplify 169^{-1/2}">
        <script type="module" src="/_nuxt/KRGuqoqh.js" crossorigin></script>
    </head>
    <body>
        <div id="__nuxt">
            <div class="header-footer-layout desktop" data-v-bff09cfc>
                <header class="desktop" data-v-bff09cfc data-v-d2bca703>
                    <div class="left-side" data-v-d2bca703>
                        <!---->
                        <span class="logo-container" aria-label="Symbolab logo" data-v-d2bca703>
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 106 33" class="nuxt-icon nuxt-icon--fill logo" data-v-d2bca703>
                                <path fill="#DB3F59" d="M34.608 22.189v-6.386c0-.786.132-1.372.396-1.76.261-.387.661-.58 1.19-.58.301-.003.596.088.844.26.284.208.516.48.676.792a3.095 3.095 0 0 1 1.116-.797c.455-.177.94-.264 1.428-.255a4.204 4.204 0 0 1 1.817.372c.537.26 1.005.645 1.362 1.123a4.72 4.72 0 0 1 1.47-1.148 4.088 4.088 0 0 1 1.737-.347c1.138 0 2.023.364 2.655 1.091.633.728.95 1.754.953 3.079v4.556c0 .78-.132 1.362-.397 1.743-.264.381-.665.572-1.202.57-.54 0-.938-.19-1.19-.565-.253-.377-.393-.96-.393-1.748V18.6c0-.833-.117-1.443-.35-1.83-.238-.386-.601-.58-1.101-.58-.556 0-.96.19-1.213.57-.254.381-.382.981-.386 1.801v3.63c0 .781-.132 1.362-.395 1.744-.264.38-.663.57-1.198.567-.54 0-.941-.19-1.205-.571-.263-.38-.395-.962-.395-1.743V18.6c0-.839-.113-1.451-.344-1.834-.23-.384-.595-.576-1.087-.576-.555 0-.96.19-1.213.57-.253.381-.382.981-.386 1.801v3.63c0 .781-.131 1.362-.395 1.744-.263.38-.664.571-1.203.57-.54 0-.94-.19-1.2-.57-.26-.38-.39-.966-.39-1.747Z"></path>
                                <path fill="#DB3F59" fill-rule="evenodd" d="M57.084 13.532a3.669 3.669 0 0 0-1.15.678l-.004-2.9c.001-.786-.13-1.37-.394-1.75-.263-.38-.665-.571-1.205-.571-.535-.003-.934.187-1.195.568-.26.382-.391.965-.391 1.75V22.19c0 .782.13 1.363.391 1.743.26.38.66.571 1.199.571.3.002.595-.087.844-.256.28-.202.512-.465.676-.768.312.35.7.626 1.135.806.46.188.953.282 1.45.276 1.33.002 2.48-.541 3.446-1.628.967-1.087 1.45-2.397 1.45-3.93.002-1.627-.47-2.984-1.416-4.07-.946-1.086-2.105-1.63-3.48-1.63a3.969 3.969 0 0 0-1.356.228Zm-.62 7.34c-.39-.487-.585-1.128-.585-1.93 0-.806.196-1.458.588-1.954a1.907 1.907 0 0 1 3.03.006c.392.511.588 1.16.588 1.948 0 .787-.199 1.427-.595 1.92a1.927 1.927 0 0 1-3.025.01ZM66.59 14.924c-1.017 1.065-1.524 2.425-1.524 4.078-.001 1.652.507 3.013 1.523 4.083 1.017 1.07 2.309 1.604 3.875 1.604 1.572-.001 2.862-.534 3.87-1.598 1.006-1.064 1.51-2.427 1.51-4.089-.002-1.66-.505-3.022-1.51-4.084-1.006-1.063-2.296-1.594-3.87-1.594-1.567 0-2.859.534-3.875 1.6Zm2.355 6.002c-.39-.497-.583-1.15-.583-1.964v-.005c0-.783.197-1.419.588-1.908a1.907 1.907 0 0 1 3.021 0c.397.495.596 1.132.596 1.913 0 .807-.194 1.46-.583 1.958a1.92 1.92 0 0 1-3.039.006Z" clip-rule="evenodd"></path>
                                <path fill="#DB3F59" d="M77.521 11.306c0-.785.132-1.369.395-1.75.264-.381.665-.57 1.204-.567.527 0 .92.192 1.18.575.26.382.39.967.39 1.746v10.882c0 .79-.129 1.371-.386 1.748-.257.378-.65.566-1.184.566-.534 0-.94-.19-1.204-.57-.263-.38-.395-.963-.395-1.744V11.306Z"></path>
                                <path fill="#DB3F59" fill-rule="evenodd" d="M88.679 24.3a3.197 3.197 0 0 0 1.171-.9c.132.328.346.617.623.837.263.182.578.276.899.266.527 0 .919-.189 1.18-.571.26-.382.388-.962.388-1.743v-6.386c0-.786-.128-1.368-.384-1.741-.26-.374-.658-.561-1.19-.561a1.52 1.52 0 0 0-.86.256 2.078 2.078 0 0 0-.66.758 3.04 3.04 0 0 0-1.111-.857 3.554 3.554 0 0 0-1.429-.278c-1.383.003-2.555.545-3.515 1.627-.96 1.081-1.44 2.413-1.44 3.995-.001 1.598.464 2.933 1.395 4.003.93 1.07 2.078 1.606 3.441 1.606a3.58 3.58 0 0 0 1.492-.311Zm-2.466-3.46c-.382-.473-.573-1.1-.573-1.883 0-.75.192-1.365.577-1.843a1.83 1.83 0 0 1 1.485-.702 1.812 1.812 0 0 1 1.466.712c.385.472.578 1.082.578 1.83 0 .767-.19 1.392-.574 1.873a1.787 1.787 0 0 1-1.47.725 1.813 1.813 0 0 1-1.49-.712ZM99.487 13.532a3.651 3.651 0 0 0-1.149.678v-2.9c0-.786-.133-1.37-.395-1.75-.264-.38-.666-.571-1.205-.571-.538-.003-.937.186-1.197.567-.26.381-.39.965-.39 1.75V22.19c0 .781.13 1.363.39 1.743.26.38.66.57 1.198.57.302.003.596-.087.846-.255.28-.202.51-.465.673-.768.313.35.7.626 1.134.807.46.188.954.282 1.452.276 1.33.002 2.479-.541 3.445-1.628.967-1.087 1.45-2.397 1.45-3.93 0-1.627-.472-2.984-1.415-4.07-.944-1.086-2.104-1.63-3.48-1.63a3.969 3.969 0 0 0-1.357.228Zm-.623 7.34c-.39-.486-.585-1.127-.585-1.93 0-.806.196-1.457.588-1.953a1.914 1.914 0 0 1 3.032.006c.391.511.587 1.16.587 1.948 0 .787-.199 1.427-.596 1.92a1.926 1.926 0 0 1-3.026.01ZM27.582.601H4.524C2.024.601 0 2.665 0 5.208v22.785c0 2.544 2.024 4.608 4.524 4.608h23.058c2.5 0 4.524-2.064 4.524-4.608V5.208C32.105 2.665 30.08.6 27.582.6ZM13.904 23.414c-1.024.89-2.37 1.334-4.041 1.334-1.284 0-2.38-.23-3.287-.689-.908-.46-1.362-.998-1.363-1.614-.016-.4.145-.788.44-1.062.292-.268.685-.403 1.179-.403.243 0 .753.12 1.53.364.777.243 1.431.364 1.964.364.425.013.84-.14 1.156-.423.301-.267.47-.652.463-1.053a1.383 1.383 0 0 0-.476-1.093c-.318-.275-.996-.57-2.034-.885-1.508-.447-2.56-.976-3.16-1.59-.597-.613-.896-1.437-.894-2.474 0-1.331.484-2.42 1.452-3.268.968-.847 2.223-1.27 3.765-1.269 1.138 0 2.076.203 2.815.607.738.404 1.106.908 1.104 1.51 0 .434-.13.772-.389 1.019-.26.247-.623.369-1.082.369-.256 0-.675-.085-1.254-.252-.578-.167-1.015-.251-1.31-.251-.486 0-.874.113-1.163.339a1.075 1.075 0 0 0-.435.891c0 .584.639 1.076 1.916 1.477l.691.216c1.376.458 2.38 1.038 3.008 1.737.63.7.947 1.57.953 2.61-.009 1.437-.525 2.6-1.548 3.488Zm13.256-7.295c.079-.196.144-.396.196-.6l.005-.003a2.06 2.06 0 0 0 .067-.499c0-.466-.14-.835-.42-1.107a1.567 1.567 0 0 0-1.135-.41c-.31-.01-.61.1-.842.306a2.47 2.47 0 0 0-.58.965l-1.959 5.057-1.797-4.79c-.218-.59-.448-.994-.686-1.21a1.341 1.341 0 0 0-.932-.326 1.474 1.474 0 0 0-1.096.453 1.541 1.541 0 0 0-.446 1.122c0 .166.013.333.04.497.025.134.065.264.12.39l3.214 7.475-1.31 2.834c-.083.177-.15.362-.197.551a2.195 2.195 0 0 0-.07.541c.003.474.146.848.43 1.123.283.274.668.412 1.154.412.283.006.559-.094.771-.28.211-.187.418-.525.622-1.01l4.85-11.491Z" clip-rule="evenodd"></path>
                            </svg>
                        </span>
                        <!--[-->
                        <div class="header-nav" data-v-d2bca703 data-v-6bd0ef5c>
                            <a href="/solver" aria-label="Solutions" data-v-6bd0ef5c>
                                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" class="nuxt-icon nuxt-icon--fill header-icon" data-v-6bd0ef5c>
                                    <path fill-rule="evenodd" d="M17.072 2.623c4.092 3.68 4.583 9.954 1.114 14.235l5.58 5.623c.323.359.31.91-.03 1.253a.896.896 0 0 1-1.244.03l-5.563-5.606a10.192 10.192 0 0 1-14.15-.76C-.976 13.37-.92 7.076 2.909 3.118a10.192 10.192 0 0 1 14.163-.495ZM2.482 13.615a8.417 8.417 0 0 0 7.78 5.231c4.644-.008 8.405-3.801 8.41-8.48.001-3.432-2.05-6.525-5.196-7.838a8.37 8.37 0 0 0-9.174 1.84 8.53 8.53 0 0 0-1.82 9.247Z" clip-rule="evenodd"></path>
                                </svg>
                                <span data-v-6bd0ef5c>Solutions</span>
                            </a>
                            <div class="tools-menu" data-v-6bd0ef5c data-v-40e089d6>
                                <!--[-->
                                <a href="/solver/integral-calculator" data-v-40e089d6>
                                    <!---->
                                    <span data-v-40e089d6>Integral Calculator</span>
                                </a>
                                <a href="/solver/derivative-calculator" data-v-40e089d6>
                                    <!---->
                                    <span data-v-40e089d6>Derivative Calculator</span>
                                </a>
                                <a href="/solver/algebra-calculator" data-v-40e089d6>
                                    <!---->
                                    <span data-v-40e089d6>Algebra Calculator</span>
                                </a>
                                <a href="/solver/matrix-calculator" data-v-40e089d6>
                                    <!---->
                                    <span data-v-40e089d6>Matrix Calculator</span>
                                </a>
                                <a href="/solver" data-v-40e089d6>
                                    <!---->
                                    <span data-v-40e089d6>More...</span>
                                </a>
                                <!--]-->
                            </div>
                        </div>
                        <div class="header-nav" data-v-d2bca703 data-v-6bd0ef5c>
                            <a href="/graphing-calculator" aria-label="Graphing" data-v-6bd0ef5c>
                                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" class="nuxt-icon nuxt-icon--fill header-icon" data-v-6bd0ef5c>
                                    <path fill-rule="evenodd" d="M.9 0a.9.9 0 0 1 .9.9v21.3h21.3a.9.9 0 1 1 0 1.8H.9a.9.9 0 0 1-.9-.9V.9A.9.9 0 0 1 .9 0Z" clip-rule="evenodd"></path>
                                    <path fill-rule="evenodd" d="M22.103 6.8c-3.506 0-6.881 2.247-8.257 5.916-.764 2.037-1.62 3.731-3.148 4.952-1.53 1.222-3.715 1.799-6.722 2.053a.9.9 0 1 1-.152-1.794c2.847-.24 4.619-.762 5.75-1.666 1.134-.905 1.85-2.214 2.587-4.177C13.785 7.753 17.805 5 22.102 5a.9.9 0 0 1 0 1.8Z" clip-rule="evenodd"></path>
                                </svg>
                                <span data-v-6bd0ef5c>Graphing</span>
                            </a>
                            <div class="tools-menu" data-v-6bd0ef5c data-v-40e089d6>
                                <!--[-->
                                <a href="/graphing-calculator/line" data-v-40e089d6>
                                    <!---->
                                    <span data-v-40e089d6>Line Graph Calculator</span>
                                </a>
                                <a href="/graphing-calculator/exponential-graph" data-v-40e089d6>
                                    <!---->
                                    <span data-v-40e089d6>Exponential Graph Calculator</span>
                                </a>
                                <a href="/graphing-calculator/quadratic-graph" data-v-40e089d6>
                                    <!---->
                                    <span data-v-40e089d6>Quadratic Graph Calculator</span>
                                </a>
                                <a href="/graphing-calculator/graph-of-sin" data-v-40e089d6>
                                    <!---->
                                    <span data-v-40e089d6>Sin graph Calculator</span>
                                </a>
                                <a href="/graphing-calculator" data-v-40e089d6>
                                    <!---->
                                    <span data-v-40e089d6>More...</span>
                                </a>
                                <!--]-->
                            </div>
                        </div>
                        <div class="header-nav" data-v-d2bca703 data-v-6bd0ef5c>
                            <a href="/calculators" aria-label="Calculators" data-v-6bd0ef5c>
                                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" class="nuxt-icon nuxt-icon--fill header-icon" data-v-6bd0ef5c>
                                    <path d="M4.8 0h14.4c.994 0 1.8.895 1.8 2s-.806 2-1.8 2H4.8C3.806 4 3 3.105 3 2s.806-2 1.8-2ZM5 8a2 2 0 1 0 0 4 2 2 0 0 0 0-4ZM3 16a2 2 0 1 1 4 0 2 2 0 0 1-4 0ZM12 8a2 2 0 1 0 0 4 2 2 0 0 0 0-4ZM10 16a2 2 0 1 1 4 0 2 2 0 0 1-4 0ZM19 8a2 2 0 1 0 0 4 2 2 0 0 0 0-4ZM17 16a2 2 0 1 1 4 0 2 2 0 0 1-4 0ZM5 20a2 2 0 1 0 0 4 2 2 0 0 0 0-4ZM10 22a2 2 0 1 1 4 0 2 2 0 0 1-4 0ZM19 20a2 2 0 1 0 0 4 2 2 0 0 0 0-4Z"></path>
                                </svg>
                                <span data-v-6bd0ef5c>Calculators</span>
                            </a>
                            <div class="tools-menu" data-v-6bd0ef5c data-v-40e089d6>
                                <!--[-->
                                <a href="/calculator/fitness/bmi" data-v-40e089d6>
                                    <!---->
                                    <span data-v-40e089d6>BMI Calculator</span>
                                </a>
                                <a href="/calculator/finance/compound_interest_rate" data-v-40e089d6>
                                    <!---->
                                    <span data-v-40e089d6>Compound Interest Calculator</span>
                                </a>
                                <a href="/calculator/math/percentage" data-v-40e089d6>
                                    <!---->
                                    <span data-v-40e089d6>Percentage Calculator</span>
                                </a>
                                <a href="/calculator/physics/acceleration" data-v-40e089d6>
                                    <!---->
                                    <span data-v-40e089d6>Acceleration Calculator</span>
                                </a>
                                <a href="/calculators" data-v-40e089d6>
                                    <!---->
                                    <span data-v-40e089d6>More...</span>
                                </a>
                                <!--]-->
                            </div>
                        </div>
                        <div class="header-nav" data-v-d2bca703 data-v-6bd0ef5c>
                            <a href="/geometry-calculator" aria-label="Geometry" data-v-6bd0ef5c>
                                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" class="nuxt-icon nuxt-icon--fill header-icon" data-v-6bd0ef5c>
                                    <path fill-rule="evenodd" d="M17.18 7.599a.958.958 0 0 0 0-1.325.888.888 0 0 0-1.284 0L.266 22.401a.958.958 0 0 0-.197 1.02c.14.35.472.579.839.579h22.184c.502 0 .908-.42.908-.936 0-.518-.406-.937-.908-.937h-9.298c-.083-3.006-1.087-5.677-3.524-7.4L17.18 7.6Zm-8.219 8.48L3.1 22.126h8.895c-.085-2.69-1.005-4.771-3.033-6.049Z" clip-rule="evenodd"></path>
                                </svg>
                                <span data-v-6bd0ef5c>Geometry</span>
                            </a>
                            <div class="tools-menu" data-v-6bd0ef5c data-v-40e089d6>
                                <!--[-->
                                <a href="/geometry-calculator/pythagorean-theorem-calculator" data-v-40e089d6>
                                    <!---->
                                    <span data-v-40e089d6>Pythagorean Theorem Calculator</span>
                                </a>
                                <a href="/geometry-calculator/circle-area-diameter-calculator" data-v-40e089d6>
                                    <!---->
                                    <span data-v-40e089d6>Circle Area Calculator</span>
                                </a>
                                <a href="/geometry-calculator/isosceles-triangle-prove-angles-calculator" data-v-40e089d6>
                                    <!---->
                                    <span data-v-40e089d6>Isosceles Triangle Calculator</span>
                                </a>
                                <a href="/geometry-calculator/triangle-perimeter-calculator" data-v-40e089d6>
                                    <!---->
                                    <span data-v-40e089d6>Triangles Calculator</span>
                                </a>
                                <a href="/geometry-calculator" data-v-40e089d6>
                                    <!---->
                                    <span data-v-40e089d6>More...</span>
                                </a>
                                <!--]-->
                            </div>
                        </div>
                        <div class="header-nav" data-v-d2bca703 data-v-6bd0ef5c>
                            <a href="#" aria-label="Tools" data-v-6bd0ef5c>
                                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 25" class="nuxt-icon nuxt-icon--fill header-icon" data-v-6bd0ef5c>
                                    <path fill-rule="evenodd" d="M12.334 4.187a.9.9 0 0 0-.668 0L.739 8.557a.9.9 0 0 0 0 1.672l3.845 1.538v5.452c0 1.378 1.072 2.442 2.406 3.11 1.375.687 3.178 1.048 5.01 1.048 1.832 0 3.634-.361 5.01-1.049 1.333-.667 2.406-1.731 2.406-3.109v-5.452l2.61-1.044v5.226a.9.9 0 0 0 1.8 0V9.393a.9.9 0 0 0-.565-.835L12.334 4.187Zm5.282 8.3L12.334 14.6a.9.9 0 0 1-.668 0l-5.282-2.113v4.732c0 .35.3.944 1.41 1.5 1.07.533 2.581.858 4.206.858 1.624 0 3.137-.325 4.205-.859 1.11-.555 1.411-1.148 1.411-1.499v-4.732ZM12 12.795l8.503-3.402L12 5.992 3.497 9.393 12 12.795Z" clip-rule="evenodd"></path>
                                </svg>
                                <span data-v-6bd0ef5c>Tools</span>
                            </a>
                            <div class="tools-menu" data-v-6bd0ef5c data-v-40e089d6>
                                <!--[-->
                                <a href="/notebook" data-v-40e089d6>
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" class="nuxt-icon nuxt-icon--fill tools-menu-icon" data-v-40e089d6>
                                        <path d="M7 5.1a.9.9 0 1 0 0 1.8h9.5a.9.9 0 1 0 0-1.8H7ZM7 9.1a.9.9 0 1 0 0 1.8h9.5a.9.9 0 1 0 0-1.8H7ZM6.1 14a.9.9 0 0 1 .9-.9h9.5a.9.9 0 1 1 0 1.8H7a.9.9 0 0 1-.9-.9Z"></path>
                                        <path fill-rule="evenodd" d="M2 23V1a1 1 0 0 1 1-1h18a1 1 0 0 1 1 1v15.914a1 1 0 0 1-.334.746l-6.81 6.086a1 1 0 0 1-.666.254H3a1 1 0 0 1-1-1Zm2-1h9.1v-5a.9.9 0 0 1 .9-.9h6V1.8L4 2v20Zm14.696-4.1L14.9 21.292V17.9h3.796Z" clip-rule="evenodd"></path>
                                    </svg>
                                    <span data-v-40e089d6>Notebook</span>
                                </a>
                                <a href="/groups" data-v-40e089d6>
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" class="nuxt-icon nuxt-icon--fill tools-menu-icon" data-v-40e089d6>
                                        <path d="M13.897 15.731a8.902 8.902 0 0 0-1.87-.998 4.771 4.771 0 0 0 1.552-3.147 6.984 6.984 0 0 1 4.917-1.996c1.451 0 2.845.437 4.03 1.263A.937.937 0 1 0 23.6 9.316a8.911 8.911 0 0 0-1.87-.998 4.769 4.769 0 0 0 1.568-3.537A4.786 4.786 0 0 0 18.517 0a4.786 4.786 0 0 0-4.781 4.78c0 1.395.6 2.653 1.556 3.527a8.875 8.875 0 0 0-2.04 1.11 4.788 4.788 0 0 0-4.438-3.002 4.786 4.786 0 0 0-4.78 4.78c0 1.392.597 2.645 1.548 3.52-2.543.952-4.605 2.999-5.444 5.608a2.785 2.785 0 0 0 .404 2.518 2.784 2.784 0 0 0 2.273 1.156h8.155a.937.937 0 1 0 0-1.875H2.815a.928.928 0 0 1-.758-.385.929.929 0 0 1-.135-.84c.927-2.88 3.753-4.892 6.872-4.892a7.01 7.01 0 0 1 4.03 1.264.938.938 0 0 0 1.073-1.538Zm4.62-13.856a2.91 2.91 0 0 1 2.905 2.906 2.91 2.91 0 0 1-2.906 2.906A2.91 2.91 0 0 1 15.61 4.78a2.91 2.91 0 0 1 2.906-2.906ZM8.813 8.29a2.91 2.91 0 0 1 2.906 2.906 2.91 2.91 0 0 1-2.906 2.906 2.91 2.91 0 0 1-2.906-2.906A2.91 2.91 0 0 1 8.814 8.29ZM24 19.545c0 .517-.42.937-.938.937h-2.577v2.578a.937.937 0 1 1-1.875 0v-2.578h-2.578a.937.937 0 0 1 0-1.875h2.578v-2.578a.937.937 0 0 1 1.875 0v2.578h2.578c.517 0 .937.42.937.938Z"></path>
                                    </svg>
                                    <span data-v-40e089d6>Groups</span>
                                </a>
                                <a href="/cheat-sheets" data-v-40e089d6>
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" class="nuxt-icon nuxt-icon--fill tools-menu-icon" data-v-40e089d6>
                                        <path fill-rule="evenodd" d="M21.5 2h-14C6.12 2 5 3.146 5 4.56v1.682a2.502 2.502 0 0 0-2.454 1.683L.15 14.66c-.472 1.329.197 2.798 1.495 3.282L14.8 22.845c1.298.483 2.732-.201 3.205-1.53l2.394-6.736c.034-.096.062-.193.085-.29H21.5c1.381 0 2.5-1.147 2.5-2.56V4.56C24 3.146 22.881 2 21.5 2Zm0 10.24c.276 0 .5-.23.5-.512V4.56a.506.506 0 0 0-.5-.512h-14c-.276 0-.5.23-.5.512v7.168c0 .283.224.512.5.512h14ZM5 8.3v3.428c0 1.414 1.12 2.56 2.5 2.56h10.875l-2.249 6.326a.497.497 0 0 1-.64.306L2.33 16.017a.516.516 0 0 1-.3-.656l2.395-6.736A.498.498 0 0 1 5 8.3Z" clip-rule="evenodd"></path>
                                        <path d="M8.922 8.339H8.51c-.281 0-.509-.21-.509-.467 0-.258.228-.467.509-.467h.677c.166 0 .321.074.416.199l1.55 2.022 1.056-4.192a.501.501 0 0 1 .495-.362h4.788c.281 0 .509.209.509.467s-.228.466-.509.466h-4.383l-1.223 4.85a.491.491 0 0 1-.398.352.524.524 0 0 1-.513-.19L8.922 8.34Z"></path>
                                        <path d="M13.828 11.215c-.249 0-.442-.173-.442-.408 0-.13.05-.229.13-.322l.854-1.001-.778-.89c-.106-.124-.156-.236-.156-.36 0-.265.2-.432.436-.432.187 0 .317.086.442.241l.617.816.629-.816c.112-.136.243-.241.411-.241.25 0 .442.173.442.408 0 .13-.055.229-.13.322l-.81.94.834.952c.106.123.156.235.156.358a.42.42 0 0 1-.436.433c-.187 0-.317-.086-.442-.241l-.673-.878-.672.878c-.113.136-.243.241-.412.241Z"></path>
                                    </svg>
                                    <span data-v-40e089d6>Cheat Sheets</span>
                                </a>
                                <a href="/worksheets/Pre-Algebra" data-v-40e089d6>
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 25" class="nuxt-icon nuxt-icon--fill tools-menu-icon" data-v-40e089d6>
                                        <path fill-rule="evenodd" d="M3.39 3.744a1.004 1.004 0 0 1 .846-1.135l14.777-2.1a.997.997 0 0 1 1.124.857l2.353 16.926a1.004 1.004 0 0 1-.846 1.135l-3.233.46v3.608a1 1 0 0 1-.994 1.005H2.495a1 1 0 0 1-.995-1.005V6.402a1 1 0 0 1 .995-1.005H3.62l-.23-1.653Zm4.016 15.878L5.274 4.289l13.2-1.875 2.132 15.333-13.2 1.875ZM3.87 7.207 5.743 20.67c.077.55.58.933 1.124.856l9.754-1.385v2.55H3.29V7.206h.58Z" clip-rule="evenodd"></path>
                                        <path d="M8.661 13.415a.253.253 0 0 0 .05.352l.992.756-.748 1.004a.253.253 0 0 0 .049.352l.397.303c.11.083.266.061.349-.05l.748-1.004.993.757c.11.083.266.061.348-.05l.3-.401a.253.253 0 0 0-.05-.352l-.992-.757.748-1.003a.253.253 0 0 0-.049-.352l-.397-.303a.247.247 0 0 0-.349.05l-.748 1.003-.993-.756a.247.247 0 0 0-.348.05l-.3.401ZM13.544 8.14a.25.25 0 0 0 .281.214l1.232-.175.173 1.244a.25.25 0 0 0 .28.214l.493-.07a.251.251 0 0 0 .212-.284l-.173-1.244 1.231-.175a.25.25 0 0 0 .212-.284l-.07-.498a.25.25 0 0 0-.28-.214l-1.232.175L15.73 5.8a.25.25 0 0 0-.28-.214l-.493.07a.25.25 0 0 0-.212.284l.173 1.244-1.231.175a.25.25 0 0 0-.212.284l.07.498ZM9.854 6.887a.502.502 0 0 1-.423.568.498.498 0 0 1-.562-.428.502.502 0 0 1 .423-.568.498.498 0 0 1 .562.428ZM7.915 9.193a.25.25 0 0 1-.281-.214l-.07-.497a.25.25 0 0 1 .212-.284l3.448-.49a.25.25 0 0 1 .28.214l.07.498a.25.25 0 0 1-.211.284l-3.448.49ZM9.846 10.442a.502.502 0 0 0 .424-.568.498.498 0 0 0-.562-.428.502.502 0 0 0-.424.568c.039.275.29.467.562.428ZM14.76 15.075a.25.25 0 0 1-.281-.214l-.07-.498a.25.25 0 0 1 .212-.284l3.448-.49a.25.25 0 0 1 .281.214l.07.498a.251.251 0 0 1-.212.284l-3.448.49ZM14.552 13.581a.25.25 0 0 1-.28-.214l-.07-.498a.25.25 0 0 1 .212-.284l3.447-.49a.25.25 0 0 1 .281.214l.07.498a.251.251 0 0 1-.212.284l-3.448.49Z"></path>
                                    </svg>
                                    <span data-v-40e089d6>Worksheets</span>
                                </a>
                                <a href="/practice" data-v-40e089d6>
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" class="nuxt-icon nuxt-icon--fill tools-menu-icon" data-v-40e089d6>
                                        <path fill-rule="evenodd" d="M4 13c0 .552-.341 1-.762 1H.762C.342 14 0 13.552 0 13s.341-1 .762-1h2.476c.42 0 .762.448.762 1ZM12 4c-.552 0-1-.341-1-.762V.762c0-.42.448-.762 1-.762s1 .341 1 .762v2.476c0 .42-.448.762-1 .762ZM19.389 6.707c-.391-.39-.467-.948-.169-1.245l1.75-1.751c.299-.298.856-.223 1.247.168.39.39.466.948.169 1.245l-1.751 1.751c-.298.298-.856.223-1.247-.168ZM4.536 6.707c.39-.39.466-.948.168-1.245L2.954 3.71c-.298-.298-.856-.223-1.247.168-.39.39-.466.948-.168 1.245l1.75 1.751c.298.298.856.223 1.247-.168ZM24 13c0 .552-.341 1-.762 1h-2.476c-.42 0-.762-.448-.762-1s.341-1 .762-1h2.476c.42 0 .762.448.762 1ZM9 23c0-.552.495-1 1.105-1h3.79c.61 0 1.105.448 1.105 1s-.495 1-1.105 1h-3.79C9.495 24 9 23.552 9 23ZM5 12c0 1.89.749 3.605 1.966 4.864l.655 2.621A2 2 0 0 0 9.561 21h4.877a2 2 0 0 0 1.94-1.515l.656-2.62A7 7 0 1 0 5 12Zm9.688 6H9.312l.155.621a.5.5 0 0 0 .485.379h4.096a.5.5 0 0 0 .485-.379l.155-.621Zm.908-2.526a1.996 1.996 0 0 0-.37.536.818.818 0 0 0-.13-.01H8.904a.817.817 0 0 0-.128.01 2 2 0 0 0-.37-.536 5 5 0 1 1 7.192 0Z" clip-rule="evenodd"></path>
                                    </svg>
                                    <span data-v-40e089d6>Practice</span>
                                </a>
                                <a href="/verify" data-v-40e089d6>
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 25" class="nuxt-icon nuxt-icon--fill tools-menu-icon" data-v-40e089d6>
                                        <path fill-rule="evenodd" d="M18.186 17.608c3.469-4.28 2.978-10.555-1.114-14.235a10.192 10.192 0 0 0-14.162.495C-.92 7.826-.976 14.12 2.779 18.148a10.192 10.192 0 0 0 14.15.76l5.563 5.605a.896.896 0 0 0 1.244-.029.913.913 0 0 0 .03-1.253l-5.58-5.623Zm-7.923 1.988a8.417 8.417 0 0 1-7.782-5.23 8.53 8.53 0 0 1 1.82-9.247 8.37 8.37 0 0 1 9.175-1.841c3.146 1.312 5.197 4.406 5.197 7.838-.006 4.679-3.767 8.472-8.41 8.48Zm4.07-11.96-4.696 4.656-1.963-1.989a.736.736 0 0 0-1.049 1.035l2.49 2.523a.736.736 0 0 0 1.125-.093l5.13-5.086a.736.736 0 0 0-1.036-1.047Z" clip-rule="evenodd"></path>
                                    </svg>
                                    <span data-v-40e089d6>Verify</span>
                                </a>
                                <!--]-->
                            </div>
                        </div>
                        <!--]-->
                    </div>
                    <!---->
                    <div class="right-side" data-v-d2bca703>
                        <div class="header-search" data-v-d2bca703 data-v-28b74b68>
                            <div class="search-container" data-v-28b74b68>
                                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" class="nuxt-icon" data-v-28b74b68>
                                    <path d="M11.681 6.238a3.525 3.525 0 0 0-2.5-1.035 3.525 3.525 0 0 0-2.5 1.035m7.902 8.345 3.75 3.75m-9.152-1.638a7.514 7.514 0 1 0 0-15.028 7.514 7.514 0 0 0 0 15.028Z"></path>
                                </svg>
                                <input placeholder="Search" value="" data-v-28b74b68>
                            </div>
                            <div style="display:none;" class="dropdown" data-v-28b74b68>
                            <!--[-->
                            <!--]-->
                            </div>
                        </div>
                        <div class="header-language" data-v-d2bca703 data-v-39804e6d>
                            <span data-v-39804e6d>en</span>
                            <div class="language-selector" data-v-39804e6d>
                                <!--[-->
                                <div class="selected" data-v-39804e6d>English</div>
                                <div class="" data-v-39804e6d>Español</div>
                                <div class="" data-v-39804e6d>Português</div>
                                <div class="" data-v-39804e6d>Français</div>
                                <div class="" data-v-39804e6d>Deutsch</div>
                                <div class="" data-v-39804e6d>Italiano</div>
                                <div class="" data-v-39804e6d>Русский</div>
                                <div class="" data-v-39804e6d>中文(简体)</div>
                                <div class="" data-v-39804e6d>한국어</div>
                                <div class="" data-v-39804e6d>日本語</div>
                                <div class="" data-v-39804e6d>Tiếng Việt</div>
                                <div class="" data-v-39804e6d>עברית</div>
                                <div class="" data-v-39804e6d>العربية</div>
                                <!--]-->
                            </div>
                        </div>
                        <div class="header-color-scheme" data-v-d2bca703 data-v-1bc384b9>
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" class="nuxt-icon" data-v-1bc384b9>
                                <path d="M16 8a8 8 0 0 0-8-8v16a8 8 0 0 0 8-8Z"></path>
                                <path fill-rule="evenodd" d="M8 14A6 6 0 1 0 8 2a6 6 0 0 0 0 12Zm0 2A8 8 0 1 0 8 0a8 8 0 0 0 0 16Z" clip-rule="evenodd"></path>
                            </svg>
                        </div>
                        <!---->
                        <!---->
                        <button class="upgrade-button" data-v-d2bca703>Upgrade</button>
                        <div class="header-avatar" data-v-d2bca703 data-v-d3dc2a2c>
                            <button aria-label="user avatar" class="avatar-button" title="" data-v-d3dc2a2c>
                                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 56 56" class="nuxt-icon" data-v-d3dc2a2c>
                                    <g fill="none" fill-rule="evenodd">
                                        <path fill="#F2B556" d="M43.31 14.962c1.872-1.185 3.123-3.258 3.123-5.637a6.68 6.68 0 0 0-6.681-6.681c-2.475 0-4.614 1.365-5.763 3.366-1.155-2.001-3.294-3.366-5.769-3.366s-4.614 1.365-5.766 3.366c-1.155-2.001-3.294-3.366-5.769-3.366a6.683 6.683 0 0 0-6.681 6.68c0 2.38 1.251 4.453 3.123 5.638C8.9 18.967 6.248 24.619 6.248 30.9c0 12.135 9.837 21.975 21.972 21.975 12.135 0 21.972-9.84 21.972-21.975 0-6.282-2.655-11.934-6.882-15.94z"></path>
                                        <path fill="#FFF" d="M38.743 34.913c0 5.985-4.851 10.836-10.836 10.836s-10.84-4.851-10.84-10.836h21.676z"></path>
                                        <path fill="#381954" fill-rule="nonzero" d="M18.118 35.913a9.84 9.84 0 0 0 9.789 8.836c5.095 0 9.284-3.873 9.785-8.836H18.118zm21.625-1c0 6.537-5.3 11.836-11.836 11.836-6.538 0-11.84-5.3-11.84-11.836a1 1 0 0 1 1-1h21.676a1 1 0 0 1 1 1z"></path>
                                        <path fill="#381954" d="M36.378 41.745a10.816 10.816 0 0 0-8.472-4.08 10.824 10.824 0 0 0-8.454 4.053s3.61 4.032 8.454 4.032c4.845 0 8.472-4.005 8.472-4.005"></path>
                                        <path fill="#FFF" d="M17.02 21.2c0-.681.123-1.33.34-1.935a4.57 4.57 0 0 0-4.26 4.56 4.575 4.575 0 0 0 4.574 4.572 4.557 4.557 0 0 0 3.534-1.674A5.74 5.74 0 0 1 17.02 21.2z"></path>
                                        <path fill="#381954" d="M17.118 19.265c-.101.58-.27 1.966.095 3.74.365 1.775 1.673 3.074 4.05 3.742.64-.776.996-1.9.996-2.984a4.497 4.497 0 0 0-4.498-4.498"></path>
                                        <path fill="#FFF" d="M38.02 21.2c0-.681.123-1.33.34-1.935a4.57 4.57 0 0 0-4.26 4.56 4.575 4.575 0 0 0 4.574 4.572 4.557 4.557 0 0 0 3.534-1.674A5.74 5.74 0 0 1 38.02 21.2z"></path>
                                        <path fill="#381954" d="M38.118 19.265c-.101.58-.27 1.966.095 3.74.365 1.775 1.673 3.074 4.05 3.742.64-.776.996-1.9.996-2.984a4.497 4.497 0 0 0-4.498-4.498"></path>
                                    </g>
                                </svg>
                                <!---->
                                <!---->
                            </button>
                            <!---->
                            <!---->
                        </div>
                    </div>
                </header>
                <!--[-->
                <div class="popular-view desktop" data-v-38a56602>
                    <div class="breadcrumbs" data-v-38a56602>
                        <div class="breadcrumbs-content" data-v-38a56602>
                            <span data-v-38a56602>Popular</span>
                            <span data-v-38a56602>&gt;</span>
                            <h1 data-v-38a56602>simplify 169^{-1/2}</h1>
                        </div>
                    </div>
                    <div class="main-content" data-v-38a56602>
                        <div class="nl-leftNav" data-v-38a56602 data-v-99b8b4c0>
                            <ul data-v-99b8b4c0>
                                <!--[-->
                                <li data-v-99b8b4c0>
                                    <a class="nl-leftMenu" href="/solver/pre-algebra-calculator" data-v-99b8b4c0>Pre Algebra</a>
                                </li>
                                <li data-v-99b8b4c0>
                                    <a class="nl-leftMenu" href="/solver/algebra-calculator" data-v-99b8b4c0>Algebra</a>
                                </li>
                                <li data-v-99b8b4c0>
                                    <a class="nl-leftMenu" href="/solver/pre-calculus-calculator" data-v-99b8b4c0>Pre Calculus</a>
                                </li>
                                <li data-v-99b8b4c0>
                                    <a class="nl-leftMenu" href="/solver/calculus-calculator" data-v-99b8b4c0>Calculus</a>
                                </li>
                                <li data-v-99b8b4c0>
                                    <a class="nl-leftMenu" href="/solver/functions-line-calculator" data-v-99b8b4c0>Functions</a>
                                </li>
                                <li data-v-99b8b4c0>
                                    <a class="nl-leftMenu" href="/solver/linear-algebra-calculator" data-v-99b8b4c0>Linear Algebra</a>
                                </li>
                                <li data-v-99b8b4c0>
                                    <a class="nl-leftMenu" href="/solver/matrix-vector-calculator" data-v-99b8b4c0>Matrices &amp;Vectors</a>
                                </li>
                                <li data-v-99b8b4c0>
                                    <a class="nl-leftMenu" href="/solver/trigonometry-calculator" data-v-99b8b4c0>Trigonometry</a>
                                </li>
                                <li data-v-99b8b4c0>
                                    <a class="nl-leftMenu" href="/solver/statistics-calculator" data-v-99b8b4c0>Statistics</a>
                                </li>
                                <li data-v-99b8b4c0>
                                    <a class="nl-leftMenu" href="/solver/physics-calculator" data-v-99b8b4c0>Physics</a>
                                </li>
                                <li data-v-99b8b4c0>
                                    <a class="nl-leftMenu" href="/solver/chemistry-calculator" data-v-99b8b4c0>Chemistry</a>
                                </li>
                                <li data-v-99b8b4c0>
                                    <a class="nl-leftMenu" href="/solver/finance-calculator" data-v-99b8b4c0>Finance</a>
                                </li>
                                <li data-v-99b8b4c0>
                                    <a class="nl-leftMenu" href="/solver/economics-calculator" data-v-99b8b4c0>Economics</a>
                                </li>
                                <li data-v-99b8b4c0>
                                    <a class="nl-leftMenu" href="/solver/conversion-calculator" data-v-99b8b4c0>Conversions</a>
                                </li>
                                <!--]-->
                            </ul>
                        </div>
                        <div class="popular-container" data-v-38a56602>
                            <div data-v-38a56602>
                                <h2 class="box-title" data-v-38a56602>Solution</h2>
                                <div class="solution-container" data-v-38a56602>
                                    <div class="solution" data-v-38a56602 data-v-a1d9f1fc>
                                        <span class="query-math" data-v-a1d9f1fc>
                                            <!--[-->
                                            <span class="mathquill-text" data-v-a1d9f1fc>simplify </span>
                                            <span class="sy-katex" data-v-a1d9f1fc data-v-7862221b>
                                                <span class="katex-display">
                                                    <span class="katex">
                                                        <span class="katex-html" aria-hidden="true">
                                                            <span class="base">
                                                                <span class="strut" style="height:1.004em;"></span>
                                                                <span class="mord">16</span>
                                                                <span class="mord">
                                                                    <span class="mord">9</span>
                                                                    <span class="msupsub">
                                                                        <span class="vlist-t">
                                                                            <span class="vlist-r">
                                                                                <span class="vlist" style="height:1.004em;">
                                                                                    <span style="top:-3.413em;margin-right:0.05em;">
                                                                                        <span class="pstrut" style="height:3em;"></span>
                                                                                        <span class="sizing reset-size6 size3 mtight">
                                                                                            <span class="mord mtight">
                                                                                                <span class="mord mtight">−</span>
                                                                                                <span class="mord mtight">
                                                                                                    <span class="mopen nulldelimiter sizing reset-size3 size6"></span>
                                                                                                    <span class="mfrac">
                                                                                                        <span class="vlist-t vlist-t2">
                                                                                                            <span class="vlist-r">
                                                                                                                <span class="vlist" style="height:0.8443em;">
                                                                                                                    <span style="top:-2.656em;">
                                                                                                                        <span class="pstrut" style="height:3em;"></span>
                                                                                                                        <span class="sizing reset-size3 size1 mtight">
                                                                                                                            <span class="mord mtight">
                                                                                                                                <span class="mord mtight">2</span>
                                                                                                                            </span>
                                                                                                                        </span>
                                                                                                                    </span>
                                                                                                                    <span style="top:-3.2255em;">
                                                                                                                        <span class="pstrut" style="height:3em;"></span>
                                                                                                                        <span class="frac-line mtight" style="border-bottom-width:0.049em;"></span>
                                                                                                                    </span>
                                                                                                                    <span style="top:-3.384em;">
                                                                                                                        <span class="pstrut" style="height:3em;"></span>
                                                                                                                        <span class="sizing reset-size3 size1 mtight">
                                                                                                                            <span class="mord mtight">
                                                                                                                                <span class="mord mtight">1</span>
                                                                                                                            </span>
                                                                                                                        </span>
                                                                                                                    </span>
                                                                                                                </span>
                                                                                                                <span class="vlist-s">​</span>
                                                                                                            </span>
                                                                                                            <span class="vlist-r">
                                                                                                                <span class="vlist" style="height:0.344em;">
                                                                                                                    <span></span>
                                                                                                                </span>
                                                                                                            </span>
                                                                                                        </span>
                                                                                                    </span>
                                                                                                    <span class="mclose nulldelimiter sizing reset-size3 size6"></span>
                                                                                                </span>
                                                                                            </span>
                                                                                        </span>
                                                                                    </span>
                                                                                </span>
                                                                            </span>
                                                                        </span>
                                                                    </span>
                                                                </span>
                                                            </span>
                                                        </span>
                                                    </span>
                                                </span>
                                            </span>
                                            <!--]-->
                                        </span>
                                        <h2 class="solution-title" data-v-a1d9f1fc>Solution</h2>
                                        <div class="solution-container" data-v-a1d9f1fc>
                                            <span class="solution-math" data-v-a1d9f1fc>
                                                <!--[-->
                                                <span class="sy-katex own-line" data-v-a1d9f1fc data-v-7862221b>
                                                    <span class="katex-display">
                                                        <span class="katex">
                                                            <span class="katex-html" aria-hidden="true">
                                                                <span class="base">
                                                                    <span class="strut" style="height:2.0074em;vertical-align:-0.686em;"></span>
                                                                    <span class="mord">
                                                                        <span class="mopen nulldelimiter"></span>
                                                                        <span class="mfrac">
                                                                            <span class="vlist-t vlist-t2">
                                                                                <span class="vlist-r">
                                                                                    <span class="vlist" style="height:1.3214em;">
                                                                                        <span style="top:-2.314em;">
                                                                                            <span class="pstrut" style="height:3em;"></span>
                                                                                            <span class="mord">
                                                                                                <span class="mord">13</span>
                                                                                            </span>
                                                                                        </span>
                                                                                        <span style="top:-3.23em;">
                                                                                            <span class="pstrut" style="height:3em;"></span>
                                                                                            <span class="frac-line" style="border-bottom-width:0.04em;"></span>
                                                                                        </span>
                                                                                        <span style="top:-3.677em;">
                                                                                            <span class="pstrut" style="height:3em;"></span>
                                                                                            <span class="mord">
                                                                                                <span class="mord">1</span>
                                                                                            </span>
                                                                                        </span>
                                                                                    </span>
                                                                                    <span class="vlist-s">​</span>
                                                                                </span>
                                                                                <span class="vlist-r">
                                                                                    <span class="vlist" style="height:0.686em;">
                                                                                        <span></span>
                                                                                    </span>
                                                                                </span>
                                                                            </span>
                                                                        </span>
                                                                        <span class="mclose nulldelimiter"></span>
                                                                    </span>
                                                                </span>
                                                            </span>
                                                        </span>
                                                    </span>
                                                </span>
                                                <!--]-->
                                            </span>
                                            <div class="open format-indicator" data-v-a1d9f1fc>
                                                <div class="format-indicator-number" data-v-a1d9f1fc>+1</div>
                                                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 10" class="nuxt-icon nuxt-icon--fill" data-v-a1d9f1fc>
                                                    <path d="M8.621.73c.166.148 7.123 6.948 7.123 6.948a.744.744 0 0 1 .256.557c0 .211-.09.409-.256.557l-.524.472a.947.947 0 0 1-1.238 0L8.003 3.883 2.018 9.27a.92.92 0 0 1-.62.23.922.922 0 0 1-.618-.23l-.524-.472A.745.745 0 0 1 0 8.241c0-.211.09-.409.256-.557 0 0 6.958-6.806 7.123-6.954A.922.922 0 0 1 8 .5c.236 0 .456.081.621.23Z"></path>
                                                </svg>
                                            </div>
                                        </div>
                                        <div class="other-solutions" data-v-a1d9f1fc>
                                            <!---->
                                            <!---->
                                            <!---->
                                            <div class="one-solution" data-v-a1d9f1fc>
                                                <div class="one-solution-title" data-v-a1d9f1fc>Decimal Notation</div>
                                                <span data-v-a1d9f1fc>
                                                    <!--[-->
                                                    <span class="sy-katex own-line force-no-scroll" data-v-a1d9f1fc data-v-7862221b>
                                                        <span class="katex-display">
                                                            <span class="katex">
                                                                <span class="katex-html" aria-hidden="true">
                                                                    <span class="base">
                                                                        <span class="strut" style="height:0.6444em;"></span>
                                                                        <span class="mord">0.07692</span>
                                                                        <span class="mspace" style="margin-right:0.1667em;"></span>
                                                                        <span class="minner">…</span>
                                                                    </span>
                                                                </span>
                                                            </span>
                                                        </span>
                                                    </span>
                                                    <!--]-->
                                                </span>
                                            </div>
                                        </div>
                                        <div class="show-hide-container" data-v-a1d9f1fc data-v-64550a09>
                                            <div data-v-64550a09>
                                                <div class="dashed-line" data-v-64550a09></div>
                                                <button class="hide-button" data-v-64550a09>
                                                    Hide Steps 
                                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 10" class="nuxt-icon nuxt-icon--fill" data-v-64550a09>
                                                        <path d="M8.621.73c.166.148 7.123 6.948 7.123 6.948a.744.744 0 0 1 .256.557c0 .211-.09.409-.256.557l-.524.472a.947.947 0 0 1-1.238 0L8.003 3.883 2.018 9.27a.92.92 0 0 1-.62.23.922.922 0 0 1-.618-.23l-.524-.472A.745.745 0 0 1 0 8.241c0-.211.09-.409.256-.557 0 0 6.958-6.806 7.123-6.954A.922.922 0 0 1 8 .5c.236 0 .456.081.621.23Z"></path>
                                                    </svg>
                                                </button>
                                            </div>
                                        </div>
                                        <div class="steps-title-container" data-v-a1d9f1fc>
                                            <div class="steps-title" data-v-a1d9f1fc>Solution steps</div>
                                        </div>
                                        <div class="steps-container" data-v-a1d9f1fc data-v-01787b30>
                                            <div class="input-math" data-v-01787b30>
                                                <!--[-->
                                                <span class="sy-katex own-line" data-v-01787b30 data-v-7862221b>
                                                    <span class="katex-display">
                                                        <span class="katex">
                                                            <span class="katex-html" aria-hidden="true">
                                                                <span class="base">
                                                                    <span class="strut" style="height:1.004em;"></span>
                                                                    <span class="mord">16</span>
                                                                    <span class="mord">
                                                                        <span class="mord">9</span>
                                                                        <span class="msupsub">
                                                                            <span class="vlist-t">
                                                                                <span class="vlist-r">
                                                                                    <span class="vlist" style="height:1.004em;">
                                                                                        <span style="top:-3.413em;margin-right:0.05em;">
                                                                                            <span class="pstrut" style="height:3em;"></span>
                                                                                            <span class="sizing reset-size6 size3 mtight">
                                                                                                <span class="mord mtight">
                                                                                                    <span class="mord mtight">−</span>
                                                                                                    <span class="mord mtight">
                                                                                                        <span class="mopen nulldelimiter sizing reset-size3 size6"></span>
                                                                                                        <span class="mfrac">
                                                                                                            <span class="vlist-t vlist-t2">
                                                                                                                <span class="vlist-r">
                                                                                                                    <span class="vlist" style="height:0.8443em;">
                                                                                                                        <span style="top:-2.656em;">
                                                                                                                            <span class="pstrut" style="height:3em;"></span>
                                                                                                                            <span class="sizing reset-size3 size1 mtight">
                                                                                                                                <span class="mord mtight">
                                                                                                                                    <span class="mord mtight">2</span>
                                                                                                                                </span>
                                                                                                                            </span>
                                                                                                                        </span>
                                                                                                                        <span style="top:-3.2255em;">
                                                                                                                            <span class="pstrut" style="height:3em;"></span>
                                                                                                                            <span class="frac-line mtight" style="border-bottom-width:0.049em;"></span>
                                                                                                                        </span>
                                                                                                                        <span style="top:-3.384em;">
                                                                                                                            <span class="pstrut" style="height:3em;"></span>
                                                                                                                            <span class="sizing reset-size3 size1 mtight">
                                                                                                                                <span class="mord mtight">
                                                                                                                                    <span class="mord mtight">1</span>
                                                                                                                                </span>
                                                                                                                            </span>
                                                                                                                        </span>
                                                                                                                    </span>
                                                                                                                    <span class="vlist-s">​</span>
                                                                                                                </span>
                                                                                                                <span class="vlist-r">
                                                                                                                    <span class="vlist" style="height:0.344em;">
                                                                                                                        <span></span>
                                                                                                                    </span>
                                                                                                                </span>
                                                                                                            </span>
                                                                                                        </span>
                                                                                                        <span class="mclose nulldelimiter sizing reset-size3 size6"></span>
                                                                                                    </span>
                                                                                                </span>
                                                                                            </span>
                                                                                        </span>
                                                                                    </span>
                                                                                </span>
                                                                            </span>
                                                                        </span>
                                                                    </span>
                                                                </span>
                                                            </span>
                                                        </span>
                                                    </span>
                                                </span>
                                                <!--]-->
                                            </div>
                                            <!--[-->
                                            <!--[-->
                                            <!---->
                                            <div class="regular-step upper-level inner-step" data-v-01787b30 data-v-9172ad38>
                                                <span class="primary" data-v-9172ad38>
                                                    <!--[-->
                                                    <span class="mathquill-text" data-v-9172ad38>Factor the number:  </span>
                                                    <span class="sy-katex" data-v-9172ad38 data-v-7862221b>
                                                        <span class="katex-display">
                                                            <span class="katex">
                                                                <span class="katex-html" aria-hidden="true">
                                                                    <span class="base">
                                                                        <span class="strut" style="height:0.6444em;"></span>
                                                                        <span class="mord">169</span>
                                                                        <span class="mspace" style="margin-right:0.2778em;"></span>
                                                                        <span class="mrel">=</span>
                                                                        <span class="mspace" style="margin-right:0.2778em;"></span>
                                                                    </span>
                                                                    <span class="base">
                                                                        <span class="strut" style="height:0.8641em;"></span>
                                                                        <span class="mord">1</span>
                                                                        <span class="mord">
                                                                            <span class="mord">3</span>
                                                                            <span class="msupsub">
                                                                                <span class="vlist-t">
                                                                                    <span class="vlist-r">
                                                                                        <span class="vlist" style="height:0.8641em;">
                                                                                            <span style="top:-3.113em;margin-right:0.05em;">
                                                                                                <span class="pstrut" style="height:2.7em;"></span>
                                                                                                <span class="sizing reset-size6 size3 mtight">
                                                                                                    <span class="mord mtight">
                                                                                                        <span class="mord mtight">2</span>
                                                                                                    </span>
                                                                                                </span>
                                                                                            </span>
                                                                                        </span>
                                                                                    </span>
                                                                                </span>
                                                                            </span>
                                                                        </span>
                                                                    </span>
                                                                </span>
                                                            </span>
                                                        </span>
                                                    </span>
                                                    <!--]-->
                                                </span>
                                                <!---->
                                                <span class="result separator" data-v-9172ad38>
                                                    <!--[-->
                                                    <span class="sy-katex own-line" data-v-9172ad38 data-v-7862221b>
                                                        <span class="katex-display">
                                                            <span class="katex">
                                                                <span class="katex-html" aria-hidden="true">
                                                                    <span class="base">
                                                                        <span class="strut" style="height:0.3669em;"></span>
                                                                        <span class="mrel">=</span>
                                                                        <span class="mspace" style="margin-right:0.2778em;"></span>
                                                                    </span>
                                                                    <span class="base">
                                                                        <span class="strut" style="height:1.558em;vertical-align:-0.35em;"></span>
                                                                        <span class="minner">
                                                                            <span class="minner">
                                                                                <span class="mopen delimcenter" style="top:0em;">
                                                                                    <span class="delimsizing size1">(</span>
                                                                                </span>
                                                                                <span class="mord">1</span>
                                                                                <span class="mord">
                                                                                    <span class="mord">3</span>
                                                                                    <span class="msupsub">
                                                                                        <span class="vlist-t">
                                                                                            <span class="vlist-r">
                                                                                                <span class="vlist" style="height:0.8641em;">
                                                                                                    <span style="top:-3.113em;margin-right:0.05em;">
                                                                                                        <span class="pstrut" style="height:2.7em;"></span>
                                                                                                        <span class="sizing reset-size6 size3 mtight">
                                                                                                            <span class="mord mtight">
                                                                                                                <span class="mord mtight">2</span>
                                                                                                            </span>
                                                                                                        </span>
                                                                                                    </span>
                                                                                                </span>
                                                                                            </span>
                                                                                        </span>
                                                                                    </span>
                                                                                </span>
                                                                                <span class="mclose delimcenter" style="top:0em;">
                                                                                    <span class="delimsizing size1">)</span>
                                                                                </span>
                                                                            </span>
                                                                            <span class="msupsub">
                                                                                <span class="vlist-t">
                                                                                    <span class="vlist-r">
                                                                                        <span class="vlist" style="height:1.208em;">
                                                                                            <span style="top:-3.617em;margin-right:0.05em;">
                                                                                                <span class="pstrut" style="height:3em;"></span>
                                                                                                <span class="sizing reset-size6 size3 mtight">
                                                                                                    <span class="mord mtight">
                                                                                                        <span class="mord mtight">−</span>
                                                                                                        <span class="mord mtight">
                                                                                                            <span class="mopen nulldelimiter sizing reset-size3 size6"></span>
                                                                                                            <span class="mfrac">
                                                                                                                <span class="vlist-t vlist-t2">
                                                                                                                    <span class="vlist-r">
                                                                                                                        <span class="vlist" style="height:0.8443em;">
                                                                                                                            <span style="top:-2.656em;">
                                                                                                                                <span class="pstrut" style="height:3em;"></span>
                                                                                                                                <span class="sizing reset-size3 size1 mtight">
                                                                                                                                    <span class="mord mtight">
                                                                                                                                        <span class="mord mtight">2</span>
                                                                                                                                    </span>
                                                                                                                                </span>
                                                                                                                            </span>
                                                                                                                            <span style="top:-3.2255em;">
                                                                                                                                <span class="pstrut" style="height:3em;"></span>
                                                                                                                                <span class="frac-line mtight" style="border-bottom-width:0.049em;"></span>
                                                                                                                            </span>
                                                                                                                            <span style="top:-3.384em;">
                                                                                                                                <span class="pstrut" style="height:3em;"></span>
                                                                                                                                <span class="sizing reset-size3 size1 mtight">
                                                                                                                                    <span class="mord mtight">
                                                                                                                                        <span class="mord mtight">1</span>
                                                                                                                                    </span>
                                                                                                                                </span>
                                                                                                                            </span>
                                                                                                                        </span>
                                                                                                                        <span class="vlist-s">​</span>
                                                                                                                    </span>
                                                                                                                    <span class="vlist-r">
                                                                                                                        <span class="vlist" style="height:0.344em;">
                                                                                                                            <span></span>
                                                                                                                        </span>
                                                                                                                    </span>
                                                                                                                </span>
                                                                                                            </span>
                                                                                                            <span class="mclose nulldelimiter sizing reset-size3 size6"></span>
                                                                                                        </span>
                                                                                                    </span>
                                                                                                </span>
                                                                                            </span>
                                                                                        </span>
                                                                                    </span>
                                                                                </span>
                                                                            </span>
                                                                        </span>
                                                                    </span>
                                                                </span>
                                                            </span>
                                                        </span>
                                                    </span>
                                                    <!--]-->
                                                </span>
                                                <!---->
                                            </div>
                                            <!--]-->
                                            <!--[-->
                                            <!---->
                                            <div class="regular-step upper-level inner-step" data-v-01787b30 data-v-9172ad38>
                                                <span class="primary" data-v-9172ad38>
                                                    <!--[-->
                                                    <span class="mathquill-text" data-v-9172ad38>Apply exponent rule: </span>
                                                    <span class="sy-katex" data-v-9172ad38 data-v-7862221b>
                                                        <span class="katex-display">
                                                            <span class="katex">
                                                                <span class="katex-html" aria-hidden="true">
                                                                    <span class="base">
                                                                        <span class="strut" style="height:1.3034em;vertical-align:-0.35em;"></span>
                                                                        <span class="minner">
                                                                            <span class="minner">
                                                                                <span class="mopen delimcenter" style="top:0em;">
                                                                                    <span class="delimsizing size1">(</span>
                                                                                </span>
                                                                                <span class="mord">
                                                                                    <span class="mord mathnormal">a</span>
                                                                                    <span class="msupsub">
                                                                                        <span class="vlist-t">
                                                                                            <span class="vlist-r">
                                                                                                <span class="vlist" style="height:0.8991em;">
                                                                                                    <span style="top:-3.113em;margin-right:0.05em;">
                                                                                                        <span class="pstrut" style="height:2.7em;"></span>
                                                                                                        <span class="sizing reset-size6 size3 mtight">
                                                                                                            <span class="mord mtight">
                                                                                                                <span class="mord mathnormal mtight">b</span>
                                                                                                            </span>
                                                                                                        </span>
                                                                                                    </span>
                                                                                                </span>
                                                                                            </span>
                                                                                        </span>
                                                                                    </span>
                                                                                </span>
                                                                                <span class="mclose delimcenter" style="top:0em;">
                                                                                    <span class="delimsizing size1">)</span>
                                                                                </span>
                                                                            </span>
                                                                            <span class="msupsub">
                                                                                <span class="vlist-t">
                                                                                    <span class="vlist-r">
                                                                                        <span class="vlist" style="height:0.9534em;">
                                                                                            <span style="top:-3.352em;margin-right:0.05em;">
                                                                                                <span class="pstrut" style="height:2.7em;"></span>
                                                                                                <span class="sizing reset-size6 size3 mtight">
                                                                                                    <span class="mord mtight">
                                                                                                        <span class="mord mathnormal mtight">c</span>
                                                                                                    </span>
                                                                                                </span>
                                                                                            </span>
                                                                                        </span>
                                                                                    </span>
                                                                                </span>
                                                                            </span>
                                                                        </span>
                                                                        <span class="mspace" style="margin-right:0.2778em;"></span>
                                                                        <span class="mrel">=</span>
                                                                        <span class="mspace" style="margin-right:0.2778em;"></span>
                                                                    </span>
                                                                    <span class="base">
                                                                        <span class="strut" style="height:1.0935em;vertical-align:-0.1944em;"></span>
                                                                        <span class="mord">
                                                                            <span class="mord mathnormal">a</span>
                                                                            <span class="msupsub">
                                                                                <span class="vlist-t">
                                                                                    <span class="vlist-r">
                                                                                        <span class="vlist" style="height:0.8991em;">
                                                                                            <span style="top:-3.113em;margin-right:0.05em;">
                                                                                                <span class="pstrut" style="height:2.7em;"></span>
                                                                                                <span class="sizing reset-size6 size3 mtight">
                                                                                                    <span class="mord mtight">
                                                                                                        <span class="mord mathnormal mtight">b</span>
                                                                                                        <span class="mord mathnormal mtight">c</span>
                                                                                                    </span>
                                                                                                </span>
                                                                                            </span>
                                                                                        </span>
                                                                                    </span>
                                                                                </span>
                                                                            </span>
                                                                        </span>
                                                                        <span class="mpunct">,</span>
                                                                        <span class="mspace" style="margin-right:0.2222em;"></span>
                                                                        <span class="mspace" style="margin-right:1em;"></span>
                                                                        <span class="mspace" style="margin-right:0.2222em;"></span>
                                                                        <span class="mspace" style="margin-right:0.1667em;"></span>
                                                                        <span class="mord mathnormal">a</span>
                                                                        <span class="mspace" style="margin-right:0.2778em;"></span>
                                                                        <span class="mrel">≥</span>
                                                                        <span class="mspace" style="margin-right:0.2778em;"></span>
                                                                    </span>
                                                                    <span class="base">
                                                                        <span class="strut" style="height:0.6444em;"></span>
                                                                        <span class="mord">0</span>
                                                                    </span>
                                                                </span>
                                                            </span>
                                                        </span>
                                                    </span>
                                                    <!--]-->
                                                </span>
                                                <!---->
                                                <span class="result separator" data-v-9172ad38>
                                                    <!--[-->
                                                    <span class="sy-katex own-line" data-v-9172ad38 data-v-7862221b>
                                                        <span class="katex-display">
                                                            <span class="katex">
                                                                <span class="katex-html" aria-hidden="true">
                                                                    <span class="base">
                                                                        <span class="strut" style="height:0.3669em;"></span>
                                                                        <span class="mrel">=</span>
                                                                        <span class="mspace" style="margin-right:0.2778em;"></span>
                                                                    </span>
                                                                    <span class="base">
                                                                        <span class="strut" style="height:1.1105em;"></span>
                                                                        <span class="mord">1</span>
                                                                        <span class="mord">
                                                                            <span class="mord">3</span>
                                                                            <span class="msupsub">
                                                                                <span class="vlist-t">
                                                                                    <span class="vlist-r">
                                                                                        <span class="vlist" style="height:1.1105em;">
                                                                                            <span style="top:-3.413em;margin-right:0.05em;">
                                                                                                <span class="pstrut" style="height:3em;"></span>
                                                                                                <span class="sizing reset-size6 size3 mtight">
                                                                                                    <span class="mord mtight">
                                                                                                        <span class="mord mtight">2</span>
                                                                                                        <span class="minner mtight">
                                                                                                            <span class="mopen sizing reset-size3 size6 mtight delimcenter" style="top:0.075em;">
                                                                                                                <span class="mtight">(</span>
                                                                                                            </span>
                                                                                                            <span class="mord mtight">−</span>
                                                                                                            <span class="mord mtight">
                                                                                                                <span class="mopen nulldelimiter sizing reset-size3 size6"></span>
                                                                                                                <span class="mfrac">
                                                                                                                    <span class="vlist-t vlist-t2">
                                                                                                                        <span class="vlist-r">
                                                                                                                            <span class="vlist" style="height:0.8443em;">
                                                                                                                                <span style="top:-2.656em;">
                                                                                                                                    <span class="pstrut" style="height:3em;"></span>
                                                                                                                                    <span class="sizing reset-size3 size1 mtight">
                                                                                                                                        <span class="mord mtight">
                                                                                                                                            <span class="mord mtight">2</span>
                                                                                                                                        </span>
                                                                                                                                    </span>
                                                                                                                                </span>
                                                                                                                                <span style="top:-3.2255em;">
                                                                                                                                    <span class="pstrut" style="height:3em;"></span>
                                                                                                                                    <span class="frac-line mtight" style="border-bottom-width:0.049em;"></span>
                                                                                                                                </span>
                                                                                                                                <span style="top:-3.384em;">
                                                                                                                                    <span class="pstrut" style="height:3em;"></span>
                                                                                                                                    <span class="sizing reset-size3 size1 mtight">
                                                                                                                                        <span class="mord mtight">
                                                                                                                                            <span class="mord mtight">1</span>
                                                                                                                                        </span>
                                                                                                                                    </span>
                                                                                                                                </span>
                                                                                                                            </span>
                                                                                                                            <span class="vlist-s">​</span>
                                                                                                                        </span>
                                                                                                                        <span class="vlist-r">
                                                                                                                            <span class="vlist" style="height:0.344em;">
                                                                                                                                <span></span>
                                                                                                                            </span>
                                                                                                                        </span>
                                                                                                                    </span>
                                                                                                                </span>
                                                                                                                <span class="mclose nulldelimiter sizing reset-size3 size6"></span>
                                                                                                            </span>
                                                                                                            <span class="mclose sizing reset-size3 size6 mtight delimcenter" style="top:0.075em;">
                                                                                                                <span class="mtight">)</span>
                                                                                                            </span>
                                                                                                        </span>
                                                                                                    </span>
                                                                                                </span>
                                                                                            </span>
                                                                                        </span>
                                                                                    </span>
                                                                                </span>
                                                                            </span>
                                                                        </span>
                                                                    </span>
                                                                </span>
                                                            </span>
                                                        </span>
                                                    </span>
                                                    <!--]-->
                                                </span>
                                                <!---->
                                            </div>
                                            <!--]-->
                                            <!--[-->
                                            <div class="interim-step upper-level inner-step" data-v-01787b30 data-v-336b5e13>
                                                <div class="interim-step-main" data-v-336b5e13>
                                                    <div class="title" data-v-336b5e13>
                                                        <span class="title-text" data-v-336b5e13>
                                                            <!--[-->
                                                            <span class="sy-katex" data-v-336b5e13 data-v-7862221b>
                                                                <span class="katex-display">
                                                                    <span class="katex">
                                                                        <span class="katex-html" aria-hidden="true">
                                                                            <span class="base">
                                                                                <span class="strut" style="height:2.4em;vertical-align:-0.95em;"></span>
                                                                                <span class="mord">2</span>
                                                                                <span class="mspace" style="margin-right:0.1667em;"></span>
                                                                                <span class="minner">
                                                                                    <span class="mopen delimcenter" style="top:0em;">
                                                                                        <span class="delimsizing size3">(</span>
                                                                                    </span>
                                                                                    <span class="mord">−</span>
                                                                                    <span class="mord">
                                                                                        <span class="mopen nulldelimiter"></span>
                                                                                        <span class="mfrac">
                                                                                            <span class="vlist-t vlist-t2">
                                                                                                <span class="vlist-r">
                                                                                                    <span class="vlist" style="height:1.3214em;">
                                                                                                        <span style="top:-2.314em;">
                                                                                                            <span class="pstrut" style="height:3em;"></span>
                                                                                                            <span class="mord">
                                                                                                                <span class="mord">2</span>
                                                                                                            </span>
                                                                                                        </span>
                                                                                                        <span style="top:-3.23em;">
                                                                                                            <span class="pstrut" style="height:3em;"></span>
                                                                                                            <span class="frac-line" style="border-bottom-width:0.04em;"></span>
                                                                                                        </span>
                                                                                                        <span style="top:-3.677em;">
                                                                                                            <span class="pstrut" style="height:3em;"></span>
                                                                                                            <span class="mord">
                                                                                                                <span class="mord">1</span>
                                                                                                            </span>
                                                                                                        </span>
                                                                                                    </span>
                                                                                                    <span class="vlist-s">​</span>
                                                                                                </span>
                                                                                                <span class="vlist-r">
                                                                                                    <span class="vlist" style="height:0.686em;">
                                                                                                        <span></span>
                                                                                                    </span>
                                                                                                </span>
                                                                                            </span>
                                                                                        </span>
                                                                                        <span class="mclose nulldelimiter"></span>
                                                                                    </span>
                                                                                    <span class="mclose delimcenter" style="top:0em;">
                                                                                        <span class="delimsizing size3">)</span>
                                                                                    </span>
                                                                                </span>
                                                                                <span class="mspace" style="margin-right:0.2778em;"></span>
                                                                                <span class="mrel">=</span>
                                                                                <span class="mspace" style="margin-right:0.2778em;"></span>
                                                                            </span>
                                                                            <span class="base">
                                                                                <span class="strut" style="height:0.7278em;vertical-align:-0.0833em;"></span>
                                                                                <span class="mord">−</span>
                                                                                <span class="mord">1</span>
                                                                            </span>
                                                                        </span>
                                                                    </span>
                                                                </span>
                                                            </span>
                                                            <!--]-->
                                                        </span>
                                                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 10" class="nuxt-icon nuxt-icon--fill" data-v-336b5e13>
                                                            <path d="M8.621.73c.166.148 7.123 6.948 7.123 6.948a.744.744 0 0 1 .256.557c0 .211-.09.409-.256.557l-.524.472a.947.947 0 0 1-1.238 0L8.003 3.883 2.018 9.27a.92.92 0 0 1-.62.23.922.922 0 0 1-.618-.23l-.524-.472A.745.745 0 0 1 0 8.241c0-.211.09-.409.256-.557 0 0 6.958-6.806 7.123-6.954A.922.922 0 0 1 8 .5c.236 0 .456.081.621.23Z"></path>
                                                        </svg>
                                                    </div>
                                                    <div class="interim-content" data-v-336b5e13>
                                                    <!---->
                                                    </div>
                                                </div>
                                                <!---->
                                            </div>
                                            <!---->
                                            <!--]-->
                                            <!--[-->
                                            <!---->
                                            <div class="regular-step upper-level inner-step" data-v-01787b30 data-v-9172ad38>
                                                <!---->
                                                <!---->
                                                <span class="result separator" data-v-9172ad38>
                                                    <!--[-->
                                                    <span class="sy-katex own-line" data-v-9172ad38 data-v-7862221b>
                                                        <span class="katex-display">
                                                            <span class="katex">
                                                                <span class="katex-html" aria-hidden="true">
                                                                    <span class="base">
                                                                        <span class="strut" style="height:0.3669em;"></span>
                                                                        <span class="mrel">=</span>
                                                                        <span class="mspace" style="margin-right:0.2778em;"></span>
                                                                    </span>
                                                                    <span class="base">
                                                                        <span class="strut" style="height:0.8641em;"></span>
                                                                        <span class="mord">1</span>
                                                                        <span class="mord">
                                                                            <span class="mord">3</span>
                                                                            <span class="msupsub">
                                                                                <span class="vlist-t">
                                                                                    <span class="vlist-r">
                                                                                        <span class="vlist" style="height:0.8641em;">
                                                                                            <span style="top:-3.113em;margin-right:0.05em;">
                                                                                                <span class="pstrut" style="height:2.7em;"></span>
                                                                                                <span class="sizing reset-size6 size3 mtight">
                                                                                                    <span class="mord mtight">
                                                                                                        <span class="mord mtight">−</span>
                                                                                                        <span class="mord mtight">1</span>
                                                                                                    </span>
                                                                                                </span>
                                                                                            </span>
                                                                                        </span>
                                                                                    </span>
                                                                                </span>
                                                                            </span>
                                                                        </span>
                                                                    </span>
                                                                </span>
                                                            </span>
                                                        </span>
                                                    </span>
                                                    <!--]-->
                                                </span>
                                                <!---->
                                            </div>
                                            <!--]-->
                                            <!--[-->
                                            <!---->
                                            <div class="regular-step upper-level inner-step" data-v-01787b30 data-v-9172ad38>
                                                <span class="primary" data-v-9172ad38>
                                                    <!--[-->
                                                    <span class="mathquill-text" data-v-9172ad38>Apply exponent rule: </span>
                                                    <span class="sy-katex" data-v-9172ad38 data-v-7862221b>
                                                        <span class="katex-display">
                                                            <span class="katex">
                                                                <span class="katex-html" aria-hidden="true">
                                                                    <span class="base">
                                                                        <span class="strut" style="height:0.8641em;"></span>
                                                                        <span class="mord">
                                                                            <span class="mord mathnormal">a</span>
                                                                            <span class="msupsub">
                                                                                <span class="vlist-t">
                                                                                    <span class="vlist-r">
                                                                                        <span class="vlist" style="height:0.8641em;">
                                                                                            <span style="top:-3.113em;margin-right:0.05em;">
                                                                                                <span class="pstrut" style="height:2.7em;"></span>
                                                                                                <span class="sizing reset-size6 size3 mtight">
                                                                                                    <span class="mord mtight">
                                                                                                        <span class="mord mtight">−</span>
                                                                                                        <span class="mord mtight">1</span>
                                                                                                    </span>
                                                                                                </span>
                                                                                            </span>
                                                                                        </span>
                                                                                    </span>
                                                                                </span>
                                                                            </span>
                                                                        </span>
                                                                        <span class="mspace" style="margin-right:0.2778em;"></span>
                                                                        <span class="mrel">=</span>
                                                                        <span class="mspace" style="margin-right:0.2778em;"></span>
                                                                    </span>
                                                                    <span class="base">
                                                                        <span class="strut" style="height:2.0074em;vertical-align:-0.686em;"></span>
                                                                        <span class="mord">
                                                                            <span class="mopen nulldelimiter"></span>
                                                                            <span class="mfrac">
                                                                                <span class="vlist-t vlist-t2">
                                                                                    <span class="vlist-r">
                                                                                        <span class="vlist" style="height:1.3214em;">
                                                                                            <span style="top:-2.314em;">
                                                                                                <span class="pstrut" style="height:3em;"></span>
                                                                                                <span class="mord">
                                                                                                    <span class="mord mathnormal">a</span>
                                                                                                </span>
                                                                                            </span>
                                                                                            <span style="top:-3.23em;">
                                                                                                <span class="pstrut" style="height:3em;"></span>
                                                                                                <span class="frac-line" style="border-bottom-width:0.04em;"></span>
                                                                                            </span>
                                                                                            <span style="top:-3.677em;">
                                                                                                <span class="pstrut" style="height:3em;"></span>
                                                                                                <span class="mord">
                                                                                                    <span class="mord">1</span>
                                                                                                </span>
                                                                                            </span>
                                                                                        </span>
                                                                                        <span class="vlist-s">​</span>
                                                                                    </span>
                                                                                    <span class="vlist-r">
                                                                                        <span class="vlist" style="height:0.686em;">
                                                                                            <span></span>
                                                                                        </span>
                                                                                    </span>
                                                                                </span>
                                                                            </span>
                                                                            <span class="mclose nulldelimiter"></span>
                                                                        </span>
                                                                    </span>
                                                                </span>
                                                            </span>
                                                        </span>
                                                    </span>
                                                    <!--]-->
                                                </span>
                                                <span class="secondary" data-v-9172ad38>
                                                    <!--[-->
                                                    <span class="sy-katex" data-v-9172ad38 data-v-7862221b>
                                                        <span class="katex-display">
                                                            <span class="katex">
                                                                <span class="katex-html" aria-hidden="true">
                                                                    <span class="base">
                                                                        <span class="strut" style="height:0.8641em;"></span>
                                                                        <span class="mord">1</span>
                                                                        <span class="mord">
                                                                            <span class="mord">3</span>
                                                                            <span class="msupsub">
                                                                                <span class="vlist-t">
                                                                                    <span class="vlist-r">
                                                                                        <span class="vlist" style="height:0.8641em;">
                                                                                            <span style="top:-3.113em;margin-right:0.05em;">
                                                                                                <span class="pstrut" style="height:2.7em;"></span>
                                                                                                <span class="sizing reset-size6 size3 mtight">
                                                                                                    <span class="mord mtight">
                                                                                                        <span class="mord mtight">−</span>
                                                                                                        <span class="mord mtight">1</span>
                                                                                                    </span>
                                                                                                </span>
                                                                                            </span>
                                                                                        </span>
                                                                                    </span>
                                                                                </span>
                                                                            </span>
                                                                        </span>
                                                                        <span class="mspace" style="margin-right:0.2778em;"></span>
                                                                        <span class="mrel">=</span>
                                                                        <span class="mspace" style="margin-right:0.2778em;"></span>
                                                                    </span>
                                                                    <span class="base">
                                                                        <span class="strut" style="height:2.0074em;vertical-align:-0.686em;"></span>
                                                                        <span class="mord">
                                                                            <span class="mopen nulldelimiter"></span>
                                                                            <span class="mfrac">
                                                                                <span class="vlist-t vlist-t2">
                                                                                    <span class="vlist-r">
                                                                                        <span class="vlist" style="height:1.3214em;">
                                                                                            <span style="top:-2.314em;">
                                                                                                <span class="pstrut" style="height:3em;"></span>
                                                                                                <span class="mord">
                                                                                                    <span class="mord">13</span>
                                                                                                </span>
                                                                                            </span>
                                                                                            <span style="top:-3.23em;">
                                                                                                <span class="pstrut" style="height:3em;"></span>
                                                                                                <span class="frac-line" style="border-bottom-width:0.04em;"></span>
                                                                                            </span>
                                                                                            <span style="top:-3.677em;">
                                                                                                <span class="pstrut" style="height:3em;"></span>
                                                                                                <span class="mord">
                                                                                                    <span class="mord">1</span>
                                                                                                </span>
                                                                                            </span>
                                                                                        </span>
                                                                                        <span class="vlist-s">​</span>
                                                                                    </span>
                                                                                    <span class="vlist-r">
                                                                                        <span class="vlist" style="height:0.686em;">
                                                                                            <span></span>
                                                                                        </span>
                                                                                    </span>
                                                                                </span>
                                                                            </span>
                                                                            <span class="mclose nulldelimiter"></span>
                                                                        </span>
                                                                    </span>
                                                                </span>
                                                            </span>
                                                        </span>
                                                    </span>
                                                    <!--]-->
                                                </span>
                                                <span class="result separator" data-v-9172ad38>
                                                    <!--[-->
                                                    <span class="sy-katex own-line" data-v-9172ad38 data-v-7862221b>
                                                        <span class="katex-display">
                                                            <span class="katex">
                                                                <span class="katex-html" aria-hidden="true">
                                                                    <span class="base">
                                                                        <span class="strut" style="height:0.3669em;"></span>
                                                                        <span class="mrel">=</span>
                                                                        <span class="mspace" style="margin-right:0.2778em;"></span>
                                                                    </span>
                                                                    <span class="base">
                                                                        <span class="strut" style="height:2.0074em;vertical-align:-0.686em;"></span>
                                                                        <span class="mord">
                                                                            <span class="mopen nulldelimiter"></span>
                                                                            <span class="mfrac">
                                                                                <span class="vlist-t vlist-t2">
                                                                                    <span class="vlist-r">
                                                                                        <span class="vlist" style="height:1.3214em;">
                                                                                            <span style="top:-2.314em;">
                                                                                                <span class="pstrut" style="height:3em;"></span>
                                                                                                <span class="mord">
                                                                                                    <span class="mord">13</span>
                                                                                                </span>
                                                                                            </span>
                                                                                            <span style="top:-3.23em;">
                                                                                                <span class="pstrut" style="height:3em;"></span>
                                                                                                <span class="frac-line" style="border-bottom-width:0.04em;"></span>
                                                                                            </span>
                                                                                            <span style="top:-3.677em;">
                                                                                                <span class="pstrut" style="height:3em;"></span>
                                                                                                <span class="mord">
                                                                                                    <span class="mord">1</span>
                                                                                                </span>
                                                                                            </span>
                                                                                        </span>
                                                                                        <span class="vlist-s">​</span>
                                                                                    </span>
                                                                                    <span class="vlist-r">
                                                                                        <span class="vlist" style="height:0.686em;">
                                                                                            <span></span>
                                                                                        </span>
                                                                                    </span>
                                                                                </span>
                                                                            </span>
                                                                            <span class="mclose nulldelimiter"></span>
                                                                        </span>
                                                                    </span>
                                                                </span>
                                                            </span>
                                                        </span>
                                                    </span>
                                                    <!--]-->
                                                </span>
                                                <!---->
                                            </div>
                                            <!--]-->
                                            <!--]-->
                                        </div>
                                    </div>
                                </div>
                                <div class="advanced-calculator" data-v-38a56602>
                                    <button data-v-38a56602>
                                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" class="nuxt-icon nuxt-icon--fill" data-v-38a56602>
                                            <path d="m18.77 16.557-3.42-3.42a7.772 7.772 0 0 0 1.302-4.311C16.652 4.511 13.142 1 8.826 1 4.511 1 1 4.51 1 8.826c0 4.315 3.51 7.826 7.826 7.826 1.593 0 3.074-.48 4.312-1.301l3.419 3.42a.782.782 0 0 0 1.106 0l1.107-1.107a.782.782 0 0 0 0-1.107zM2.566 8.826a6.268 6.268 0 0 1 6.261-6.26 6.268 6.268 0 0 1 6.261 6.26 6.268 6.268 0 0 1-6.26 6.26 6.268 6.268 0 0 1-6.262-6.26z"></path>
                                        </svg>
                                        <span data-v-38a56602>Enter your problem</span>
                                    </button>
                                </div>
                                <h2 class="box-title" data-v-38a56602>Popular Examples</h2>
                                <div class="popular-examples" data-v-38a56602 data-v-953aa121>
                                    <!--[-->
                                    <!--[-->
                                    <a href="/popular-algebra/algebra-107" data-v-953aa121>factor 3x^3+27x</a>
                                    <a class="example" href="/popular-algebra/algebra-107" data-v-953aa121>
                                        <span data-v-953aa121>
                                            <!--[-->
                                            <span class="mathquill-text" data-v-953aa121>factor </span>
                                            <span class="sy-katex" data-v-953aa121 data-v-7862221b>
                                                <span class="katex-display">
                                                    <span class="katex">
                                                        <span class="katex-html" aria-hidden="true">
                                                            <span class="base">
                                                                <span class="strut" style="height:0.9474em;vertical-align:-0.0833em;"></span>
                                                                <span class="mord">3</span>
                                                                <span class="mord">
                                                                    <span class="mord mathnormal">x</span>
                                                                    <span class="msupsub">
                                                                        <span class="vlist-t">
                                                                            <span class="vlist-r">
                                                                                <span class="vlist" style="height:0.8641em;">
                                                                                    <span style="top:-3.113em;margin-right:0.05em;">
                                                                                        <span class="pstrut" style="height:2.7em;"></span>
                                                                                        <span class="sizing reset-size6 size3 mtight">
                                                                                            <span class="mord mtight">
                                                                                                <span class="mord mtight">3</span>
                                                                                            </span>
                                                                                        </span>
                                                                                    </span>
                                                                                </span>
                                                                            </span>
                                                                        </span>
                                                                    </span>
                                                                </span>
                                                                <span class="mspace" style="margin-right:0.2222em;"></span>
                                                                <span class="mbin">+</span>
                                                                <span class="mspace" style="margin-right:0.2222em;"></span>
                                                            </span>
                                                            <span class="base">
                                                                <span class="strut" style="height:0.6444em;"></span>
                                                                <span class="mord">27</span>
                                                                <span class="mord mathnormal">x</span>
                                                            </span>
                                                        </span>
                                                    </span>
                                                </span>
                                            </span>
                                            <!--]-->
                                        </span>
                                    </a>
                                    <!--]-->
                                    <!--[-->
                                    <a href="/popular-algebra/algebra-108" data-v-953aa121>simplify 7/4*2</a>
                                    <a class="example" href="/popular-algebra/algebra-108" data-v-953aa121>
                                        <span data-v-953aa121>
                                            <!--[-->
                                            <span class="mathquill-text" data-v-953aa121>simplify </span>
                                            <span class="sy-katex" data-v-953aa121 data-v-7862221b>
                                                <span class="katex-display">
                                                    <span class="katex">
                                                        <span class="katex-html" aria-hidden="true">
                                                            <span class="base">
                                                                <span class="strut" style="height:2.0074em;vertical-align:-0.686em;"></span>
                                                                <span class="mord">
                                                                    <span class="mopen nulldelimiter"></span>
                                                                    <span class="mfrac">
                                                                        <span class="vlist-t vlist-t2">
                                                                            <span class="vlist-r">
                                                                                <span class="vlist" style="height:1.3214em;">
                                                                                    <span style="top:-2.314em;">
                                                                                        <span class="pstrut" style="height:3em;"></span>
                                                                                        <span class="mord">
                                                                                            <span class="mord">4</span>
                                                                                        </span>
                                                                                    </span>
                                                                                    <span style="top:-3.23em;">
                                                                                        <span class="pstrut" style="height:3em;"></span>
                                                                                        <span class="frac-line" style="border-bottom-width:0.04em;"></span>
                                                                                    </span>
                                                                                    <span style="top:-3.677em;">
                                                                                        <span class="pstrut" style="height:3em;"></span>
                                                                                        <span class="mord">
                                                                                            <span class="mord">7</span>
                                                                                        </span>
                                                                                    </span>
                                                                                </span>
                                                                                <span class="vlist-s">​</span>
                                                                            </span>
                                                                            <span class="vlist-r">
                                                                                <span class="vlist" style="height:0.686em;">
                                                                                    <span></span>
                                                                                </span>
                                                                            </span>
                                                                        </span>
                                                                    </span>
                                                                    <span class="mclose nulldelimiter"></span>
                                                                </span>
                                                                <span class="mspace" style="margin-right:0.2222em;"></span>
                                                                <span class="mbin">⋅</span>
                                                                <span class="mspace" style="margin-right:0.2222em;"></span>
                                                                <span class="mspace" style="margin-right:0.2222em;"></span>
                                                            </span>
                                                            <span class="base">
                                                                <span class="strut" style="height:0.6444em;"></span>
                                                                <span class="mord">2</span>
                                                            </span>
                                                        </span>
                                                    </span>
                                                </span>
                                            </span>
                                            <!--]-->
                                        </span>
                                    </a>
                                    <!--]-->
                                    <!--[-->
                                    <a href="/popular-algebra/algebra-109" data-v-953aa121>|4y-3|&gt;=-9</a>
                                    <a class="example" href="/popular-algebra/algebra-109" data-v-953aa121>
                                        <span data-v-953aa121>
                                            <!--[-->
                                            <span class="sy-katex" data-v-953aa121 data-v-7862221b>
                                                <span class="katex-display">
                                                    <span class="katex">
                                                        <span class="katex-html" aria-hidden="true">
                                                            <span class="base">
                                                                <span class="strut" style="height:1em;vertical-align:-0.25em;"></span>
                                                                <span class="minner">
                                                                    <span class="mopen delimcenter" style="top:0em;">∣</span>
                                                                    <span class="mord">4</span>
                                                                    <span class="mord mathnormal" style="margin-right:0.03588em;">y</span>
                                                                    <span class="mspace" style="margin-right:0.2222em;"></span>
                                                                    <span class="mbin">−</span>
                                                                    <span class="mspace" style="margin-right:0.2222em;"></span>
                                                                    <span class="mord">3</span>
                                                                    <span class="mclose delimcenter" style="top:0em;">∣</span>
                                                                </span>
                                                                <span class="mspace" style="margin-right:0.2778em;"></span>
                                                                <span class="mrel">≥</span>
                                                                <span class="mspace" style="margin-right:0.2222em;"></span>
                                                                <span class="mspace" style="margin-right:0.2778em;"></span>
                                                            </span>
                                                            <span class="base">
                                                                <span class="strut" style="height:0.7278em;vertical-align:-0.0833em;"></span>
                                                                <span class="mord">−</span>
                                                                <span class="mord">9</span>
                                                            </span>
                                                        </span>
                                                    </span>
                                                </span>
                                            </span>
                                            <!--]-->
                                        </span>
                                    </a>
                                    <!--]-->
                                    <!--[-->
                                    <a href="/popular-algebra/algebra-110" data-v-953aa121>3x-x^2 &gt;0</a>
                                    <a class="example" href="/popular-algebra/algebra-110" data-v-953aa121>
                                        <span data-v-953aa121>
                                            <!--[-->
                                            <span class="sy-katex" data-v-953aa121 data-v-7862221b>
                                                <span class="katex-display">
                                                    <span class="katex">
                                                        <span class="katex-html" aria-hidden="true">
                                                            <span class="base">
                                                                <span class="strut" style="height:0.7278em;vertical-align:-0.0833em;"></span>
                                                                <span class="mord">3</span>
                                                                <span class="mord mathnormal">x</span>
                                                                <span class="mspace" style="margin-right:0.2222em;"></span>
                                                                <span class="mbin">−</span>
                                                                <span class="mspace" style="margin-right:0.2222em;"></span>
                                                            </span>
                                                            <span class="base">
                                                                <span class="strut" style="height:0.9032em;vertical-align:-0.0391em;"></span>
                                                                <span class="mord">
                                                                    <span class="mord mathnormal">x</span>
                                                                    <span class="msupsub">
                                                                        <span class="vlist-t">
                                                                            <span class="vlist-r">
                                                                                <span class="vlist" style="height:0.8641em;">
                                                                                    <span style="top:-3.113em;margin-right:0.05em;">
                                                                                        <span class="pstrut" style="height:2.7em;"></span>
                                                                                        <span class="sizing reset-size6 size3 mtight">
                                                                                            <span class="mord mtight">
                                                                                                <span class="mord mtight">2</span>
                                                                                            </span>
                                                                                        </span>
                                                                                    </span>
                                                                                </span>
                                                                            </span>
                                                                        </span>
                                                                    </span>
                                                                </span>
                                                                <span class="mspace" style="margin-right:0.2778em;"></span>
                                                                <span class="mrel">&gt;</span>
                                                                <span class="mspace" style="margin-right:0.2778em;"></span>
                                                            </span>
                                                            <span class="base">
                                                                <span class="strut" style="height:0.6444em;"></span>
                                                                <span class="mord">0</span>
                                                            </span>
                                                        </span>
                                                    </span>
                                                </span>
                                            </span>
                                            <!--]-->
                                        </span>
                                    </a>
                                    <!--]-->
                                    <!--[-->
                                    <a href="/popular-algebra/algebra-111" data-v-953aa121>simplify sqrt(40)</a>
                                    <a class="example" href="/popular-algebra/algebra-111" data-v-953aa121>
                                        <span data-v-953aa121>
                                            <!--[-->
                                            <span class="mathquill-text" data-v-953aa121>simplify </span>
                                            <span class="sy-katex" data-v-953aa121 data-v-7862221b>
                                                <span class="katex-display">
                                                    <span class="katex">
                                                        <span class="katex-html" aria-hidden="true">
                                                            <span class="base">
                                                                <span class="strut" style="height:1.04em;vertical-align:-0.0839em;"></span>
                                                                <span class="mord sqrt">
                                                                    <span class="vlist-t vlist-t2">
                                                                        <span class="vlist-r">
                                                                            <span class="vlist" style="height:0.9561em;">
                                                                                <span class="svg-align" style="top:-3em;">
                                                                                    <span class="pstrut" style="height:3em;"></span>
                                                                                    <span class="mord" style="padding-left:0.833em;">
                                                                                        <span class="mord">40</span>
                                                                                    </span>
                                                                                </span>
                                                                                <span style="top:-2.9161em;">
                                                                                    <span class="pstrut" style="height:3em;"></span>
                                                                                    <span class="hide-tail" style="min-width:0.853em;height:1.08em;">
                                                                                        <svg xmlns="http://www.w3.org/2000/svg" width="400em" height="1.08em" viewBox="0 0 400000 1080" preserveAspectRatio="xMinYMin slice">
                                                                                            <path d="M95,702
c-2.7,0,-7.17,-2.7,-13.5,-8c-5.8,-5.3,-9.5,-10,-9.5,-14
c0,-2,0.3,-3.3,1,-4c1.3,-2.7,23.83,-20.7,67.5,-54
c44.2,-33.3,65.8,-50.3,66.5,-51c1.3,-1.3,3,-2,5,-2c4.7,0,8.7,3.3,12,10
s173,378,173,378c0.7,0,35.3,-71,104,-213c68.7,-142,137.5,-285,206.5,-429
c69,-144,104.5,-217.7,106.5,-221
l0 -0
c5.3,-9.3,12,-14,20,-14
H400000v40H845.2724
s-225.272,467,-225.272,467s-235,486,-235,486c-2.7,4.7,-9,7,-19,7
c-6,0,-10,-1,-12,-3s-194,-422,-194,-422s-65,47,-65,47z
M834 80h400000v40h-400000z"/>
                                                                                        </svg>
                                                                                    </span>
                                                                                </span>
                                                                            </span>
                                                                            <span class="vlist-s">​</span>
                                                                        </span>
                                                                        <span class="vlist-r">
                                                                            <span class="vlist" style="height:0.0839em;">
                                                                                <span></span>
                                                                            </span>
                                                                        </span>
                                                                    </span>
                                                                </span>
                                                            </span>
                                                        </span>
                                                    </span>
                                                </span>
                                            </span>
                                            <!--]-->
                                        </span>
                                    </a>
                                    <!--]-->
                                    <!--]-->
                                </div>
                                <div data-v-38a56602>
                                    <h2 class="box-title" data-v-38a56602>Frequently Asked Questions (FAQ)</h2>
                                    <ul class="popular-faqs" data-v-38a56602 data-v-9c91cd27>
                                        <!--[-->
                                        <li data-v-9c91cd27>
                                            <h3 data-v-9c91cd27>What is 169^{-1/2} ?</h3>
                                            <div data-v-9c91cd27>The solution to 169^{-1/2} is 1/13</div>
                                        </li>
                                        <!--]-->
                                    </ul>
                                </div>
                            </div>
                        </div>
                        <div class="popular-ads ads" data-v-38a56602 data-v-6222bc7d>
                            <div class="ads-pane" data-v-6222bc7d>
                                <div class="googleAdsense print-hide" data-v-6222bc7d>
                                    <div id="SYM_solver_sidebar_1" class="googleAdsense print-hide" data-v-6222bc7d></div>
                                </div>
                                <div class="googleAdsense print-hide" data-v-6222bc7d>
                                    <div id="SYM_solver_sidebar_2" class="googleAdsense print-hide" data-v-6222bc7d></div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <!--]-->
                <div class="footer desktop" style="display:none;" data-v-bff09cfc data-v-b3dea1e9>
                    <div id="footer-top" data-v-b3dea1e9>
                        <nav data-v-b3dea1e9>
                            <div class="home-only" data-v-b3dea1e9>
                                <a href="/" aria-label="Home" data-v-b3dea1e9>
                                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 106 33" class="nuxt-icon nuxt-icon--fill logo" data-v-b3dea1e9>
                                        <path fill="#DB3F59" d="M34.608 22.189v-6.386c0-.786.132-1.372.396-1.76.261-.387.661-.58 1.19-.58.301-.003.596.088.844.26.284.208.516.48.676.792a3.095 3.095 0 0 1 1.116-.797c.455-.177.94-.264 1.428-.255a4.204 4.204 0 0 1 1.817.372c.537.26 1.005.645 1.362 1.123a4.72 4.72 0 0 1 1.47-1.148 4.088 4.088 0 0 1 1.737-.347c1.138 0 2.023.364 2.655 1.091.633.728.95 1.754.953 3.079v4.556c0 .78-.132 1.362-.397 1.743-.264.381-.665.572-1.202.57-.54 0-.938-.19-1.19-.565-.253-.377-.393-.96-.393-1.748V18.6c0-.833-.117-1.443-.35-1.83-.238-.386-.601-.58-1.101-.58-.556 0-.96.19-1.213.57-.254.381-.382.981-.386 1.801v3.63c0 .781-.132 1.362-.395 1.744-.264.38-.663.57-1.198.567-.54 0-.941-.19-1.205-.571-.263-.38-.395-.962-.395-1.743V18.6c0-.839-.113-1.451-.344-1.834-.23-.384-.595-.576-1.087-.576-.555 0-.96.19-1.213.57-.253.381-.382.981-.386 1.801v3.63c0 .781-.131 1.362-.395 1.744-.263.38-.664.571-1.203.57-.54 0-.94-.19-1.2-.57-.26-.38-.39-.966-.39-1.747Z"></path>
                                        <path fill="#DB3F59" fill-rule="evenodd" d="M57.084 13.532a3.669 3.669 0 0 0-1.15.678l-.004-2.9c.001-.786-.13-1.37-.394-1.75-.263-.38-.665-.571-1.205-.571-.535-.003-.934.187-1.195.568-.26.382-.391.965-.391 1.75V22.19c0 .782.13 1.363.391 1.743.26.38.66.571 1.199.571.3.002.595-.087.844-.256.28-.202.512-.465.676-.768.312.35.7.626 1.135.806.46.188.953.282 1.45.276 1.33.002 2.48-.541 3.446-1.628.967-1.087 1.45-2.397 1.45-3.93.002-1.627-.47-2.984-1.416-4.07-.946-1.086-2.105-1.63-3.48-1.63a3.969 3.969 0 0 0-1.356.228Zm-.62 7.34c-.39-.487-.585-1.128-.585-1.93 0-.806.196-1.458.588-1.954a1.907 1.907 0 0 1 3.03.006c.392.511.588 1.16.588 1.948 0 .787-.199 1.427-.595 1.92a1.927 1.927 0 0 1-3.025.01ZM66.59 14.924c-1.017 1.065-1.524 2.425-1.524 4.078-.001 1.652.507 3.013 1.523 4.083 1.017 1.07 2.309 1.604 3.875 1.604 1.572-.001 2.862-.534 3.87-1.598 1.006-1.064 1.51-2.427 1.51-4.089-.002-1.66-.505-3.022-1.51-4.084-1.006-1.063-2.296-1.594-3.87-1.594-1.567 0-2.859.534-3.875 1.6Zm2.355 6.002c-.39-.497-.583-1.15-.583-1.964v-.005c0-.783.197-1.419.588-1.908a1.907 1.907 0 0 1 3.021 0c.397.495.596 1.132.596 1.913 0 .807-.194 1.46-.583 1.958a1.92 1.92 0 0 1-3.039.006Z" clip-rule="evenodd"></path>
                                        <path fill="#DB3F59" d="M77.521 11.306c0-.785.132-1.369.395-1.75.264-.381.665-.57 1.204-.567.527 0 .92.192 1.18.575.26.382.39.967.39 1.746v10.882c0 .79-.129 1.371-.386 1.748-.257.378-.65.566-1.184.566-.534 0-.94-.19-1.204-.57-.263-.38-.395-.963-.395-1.744V11.306Z"></path>
                                        <path fill="#DB3F59" fill-rule="evenodd" d="M88.679 24.3a3.197 3.197 0 0 0 1.171-.9c.132.328.346.617.623.837.263.182.578.276.899.266.527 0 .919-.189 1.18-.571.26-.382.388-.962.388-1.743v-6.386c0-.786-.128-1.368-.384-1.741-.26-.374-.658-.561-1.19-.561a1.52 1.52 0 0 0-.86.256 2.078 2.078 0 0 0-.66.758 3.04 3.04 0 0 0-1.111-.857 3.554 3.554 0 0 0-1.429-.278c-1.383.003-2.555.545-3.515 1.627-.96 1.081-1.44 2.413-1.44 3.995-.001 1.598.464 2.933 1.395 4.003.93 1.07 2.078 1.606 3.441 1.606a3.58 3.58 0 0 0 1.492-.311Zm-2.466-3.46c-.382-.473-.573-1.1-.573-1.883 0-.75.192-1.365.577-1.843a1.83 1.83 0 0 1 1.485-.702 1.812 1.812 0 0 1 1.466.712c.385.472.578 1.082.578 1.83 0 .767-.19 1.392-.574 1.873a1.787 1.787 0 0 1-1.47.725 1.813 1.813 0 0 1-1.49-.712ZM99.487 13.532a3.651 3.651 0 0 0-1.149.678v-2.9c0-.786-.133-1.37-.395-1.75-.264-.38-.666-.571-1.205-.571-.538-.003-.937.186-1.197.567-.26.381-.39.965-.39 1.75V22.19c0 .781.13 1.363.39 1.743.26.38.66.57 1.198.57.302.003.596-.087.846-.255.28-.202.51-.465.673-.768.313.35.7.626 1.134.807.46.188.954.282 1.452.276 1.33.002 2.479-.541 3.445-1.628.967-1.087 1.45-2.397 1.45-3.93 0-1.627-.472-2.984-1.415-4.07-.944-1.086-2.104-1.63-3.48-1.63a3.969 3.969 0 0 0-1.357.228Zm-.623 7.34c-.39-.486-.585-1.127-.585-1.93 0-.806.196-1.457.588-1.953a1.914 1.914 0 0 1 3.032.006c.391.511.587 1.16.587 1.948 0 .787-.199 1.427-.596 1.92a1.926 1.926 0 0 1-3.026.01ZM27.582.601H4.524C2.024.601 0 2.665 0 5.208v22.785c0 2.544 2.024 4.608 4.524 4.608h23.058c2.5 0 4.524-2.064 4.524-4.608V5.208C32.105 2.665 30.08.6 27.582.6ZM13.904 23.414c-1.024.89-2.37 1.334-4.041 1.334-1.284 0-2.38-.23-3.287-.689-.908-.46-1.362-.998-1.363-1.614-.016-.4.145-.788.44-1.062.292-.268.685-.403 1.179-.403.243 0 .753.12 1.53.364.777.243 1.431.364 1.964.364.425.013.84-.14 1.156-.423.301-.267.47-.652.463-1.053a1.383 1.383 0 0 0-.476-1.093c-.318-.275-.996-.57-2.034-.885-1.508-.447-2.56-.976-3.16-1.59-.597-.613-.896-1.437-.894-2.474 0-1.331.484-2.42 1.452-3.268.968-.847 2.223-1.27 3.765-1.269 1.138 0 2.076.203 2.815.607.738.404 1.106.908 1.104 1.51 0 .434-.13.772-.389 1.019-.26.247-.623.369-1.082.369-.256 0-.675-.085-1.254-.252-.578-.167-1.015-.251-1.31-.251-.486 0-.874.113-1.163.339a1.075 1.075 0 0 0-.435.891c0 .584.639 1.076 1.916 1.477l.691.216c1.376.458 2.38 1.038 3.008 1.737.63.7.947 1.57.953 2.61-.009 1.437-.525 2.6-1.548 3.488Zm13.256-7.295c.079-.196.144-.396.196-.6l.005-.003a2.06 2.06 0 0 0 .067-.499c0-.466-.14-.835-.42-1.107a1.567 1.567 0 0 0-1.135-.41c-.31-.01-.61.1-.842.306a2.47 2.47 0 0 0-.58.965l-1.959 5.057-1.797-4.79c-.218-.59-.448-.994-.686-1.21a1.341 1.341 0 0 0-.932-.326 1.474 1.474 0 0 0-1.096.453 1.541 1.541 0 0 0-.446 1.122c0 .166.013.333.04.497.025.134.065.264.12.39l3.214 7.475-1.31 2.834c-.083.177-.15.362-.197.551a2.195 2.195 0 0 0-.07.541c.003.474.146.848.43 1.123.283.274.668.412 1.154.412.283.006.559-.094.771-.28.211-.187.418-.525.622-1.01l4.85-11.491Z" clip-rule="evenodd"></path>
                                    </svg>
                                </a>
                            </div>
                            <div class="footer-links" data-v-b3dea1e9>
                                <div class="footer-links-section" data-v-b3dea1e9>
                                    <span class="footer-title" data-v-b3dea1e9>Study Tools</span>
                                    <a href="/" data-v-b3dea1e9>AI Math Solver</a>
                                    <a href="/popular-algebra" data-v-b3dea1e9>Popular Problems</a>
                                    <a href="/worksheets/Pre-Algebra" data-v-b3dea1e9>Worksheets</a>
                                    <a href="/study-guides" data-v-b3dea1e9>Study Guides</a>
                                    <a href="/practice" data-v-b3dea1e9>Practice</a>
                                    <a id="cheat-sheets" href="/cheat-sheets" data-v-b3dea1e9>Cheat Sheets</a>
                                    <a id="calculator-title" href="/calculators" data-v-b3dea1e9>Calculators</a>
                                    <a id="graphing-calculator" href="/graphing-calculator" data-v-b3dea1e9>Graphing Calculator</a>
                                    <a href="/geometry-calculator" data-v-b3dea1e9>Geometry Calculator</a>
                                    <a href="/verify" data-v-b3dea1e9>Verify Solution</a>
                                </div>
                                <div class="footer-links-section" data-v-b3dea1e9>
                                    <span class="footer-title" data-v-b3dea1e9>Apps</span>
                                    <a href="https://play.google.com/store/apps/details?id=com.devsense.symbolab" data-v-b3dea1e9>Symbolab App (Android)</a>
                                    <a href="https://play.google.com/store/apps/details?id=com.symbolab.graphingcalculator" data-v-b3dea1e9>Graphing Calculator (Android)</a>
                                    <a href="https://play.google.com/store/apps/details?id=com.symbolab.practice" data-v-b3dea1e9>Practice (Android)</a>
                                    <a href="https://apps.apple.com/us/app/id876942533" data-v-b3dea1e9>Symbolab App (iOS)</a>
                                    <a href="https://apps.apple.com/us/app/id1435182798" data-v-b3dea1e9>Graphing Calculator (iOS)</a>
                                    <a href="https://apps.apple.com/us/app/id1469186281" data-v-b3dea1e9>Practice (iOS)</a>
                                    <a href="https://chromewebstore.google.com/detail/mgfcnnpakbfcefgphceolkjldjfpieff" target="_blank" data-v-b3dea1e9>Chrome Extension</a>
                                    <a href="/math-solver-api" class="" data-v-b3dea1e9>Symbolab Math Solver API</a>
                                </div>
                                <div class="footer-links-section" data-v-b3dea1e9>
                                    <span class="footer-title" data-v-b3dea1e9>Company</span>
                                    <a class="about" href="/about" data-v-b3dea1e9>About Symbolab</a>
                                    <a href="https://blog.symbolab.com" data-v-b3dea1e9>Blog</a>
                                    <a href="/help" data-v-b3dea1e9>Help</a>
                                    <button class="contact-us" data-v-b3dea1e9>Contact Us</button>
                                    <!---->
                                    <!---->
                                </div>
                                <div class="footer-links-section" data-v-b3dea1e9>
                                    <span class="footer-title" data-v-b3dea1e9>Legal</span>
                                    <a href="/privacy-policy" data-v-b3dea1e9>Privacy</a>
                                    <a href="/public/terms.pdf" data-v-b3dea1e9>Terms</a>
                                    <a href="/cookie-policy" data-v-b3dea1e9>Cookie Policy</a>
                                    <span id="cookie-settings-link" onclick="OneTrust.ToggleInfoDisplay();" class="span-footer-link cookie-settings-link" data-v-b3dea1e9>Cookie Settings</span>
                                    <span style="display:none;" id="cookie-settings-link-sell" onclick="OneTrust.ToggleInfoDisplay();" class="span-footer-link cookie-settings-link" data-v-b3dea1e9>Do Not Sell or Share My Personal Info</span>
                                    <span class="footer-title" data-v-b3dea1e9>Copyright, Community Guidelines, DSA &amp;other Legal Resources</span>
                                    <a href="https://learneo.com/legal" data-v-b3dea1e9>Learneo Legal Center</a>
                                </div>
                            </div>
                            <div class="social-media-panel" data-v-b3dea1e9>
                                <button class="feedback-button contact-us" data-v-b3dea1e9>
                                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="nuxt-icon" data-v-b3dea1e9>
                                        <path fill="#fff" d="M13.85 11.35c-.41 0-.75-.34-.75-.75V8.39c0-.2.08-.39.22-.53l6.6-6.64a.75.75 0 0 1 1.06 0l2.2 2.21c.29.29.29.77 0 1.06l-6.6 6.63a.75.75 0 0 1-.53.22h-2.2v.01Zm1.89-1.51 5.85-5.88-1.14-1.15-5.85 5.88v1.15h1.14Z"></path>
                                        <path fill="#fff" d="M9.45 22.4c-.41 0-.75-.34-.75-.75v-2.56H3.95C2.33 19.09 1 17.76 1 16.13V6.17c0-1.63 1.33-2.96 2.95-2.96h9.9c.41 0 .75.34.75.75s-.34.75-.75.75h-9.9c-.8 0-1.45.65-1.45 1.46v9.95c0 .8.65 1.46 1.45 1.46h5.5c.41 0 .75.34.75.75v1.81l3.2-2.41c.13-.1.29-.15.45-.15h5.5c.8 0 1.45-.66 1.45-1.46V8.38a.749.749 0 1 1 1.5 0v7.74c0 1.63-1.33 2.96-2.95 2.96H14.1l-4.2 3.17c-.13.1-.29.15-.45.15Z"></path>
                                        <path fill="#fff" d="M5.05 8.03c-.41 0-.75-.34-.75-.75s.34-.75.75-.75h5.5c.41 0 .75.34.75.75s-.34.75-.75.75h-5.5ZM5.05 11.35c-.41 0-.75-.34-.75-.75s.34-.75.75-.75h5.5c.41 0 .75.34.75.75s-.34.75-.75.75h-5.5ZM5.05 14.66c-.41 0-.75-.34-.75-.75s.34-.75.75-.75h13.2c.41 0 .75.34.75.75s-.34.75-.75.75H5.05Z"></path>
                                    </svg>
                                    <span data-v-b3dea1e9>Feedback</span>
                                </button>
                                <span class="footer-title social-title" data-v-b3dea1e9>Social Media</span>
                                <div id="social-buttons" data-v-b3dea1e9>
                                    <a class="nl-social2" href="/cdn-cgi/l/email-protection#75161a1b0114160135060c18171a1914175b161a18" data-v-b3dea1e9>
                                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="nuxt-icon" aria-label="Email us" data-v-b3dea1e9>
                                            <path fill="#DB3F59" d="M21.89 3.563H2.11C.943 3.563 0 4.513 0 5.671v12.656c0 1.167.95 2.11 2.11 2.11h19.78c1.156 0 2.11-.94 2.11-2.11V5.672c0-1.158-.94-2.11-2.11-2.11Zm-.295 1.406-8.103 8.06a2.096 2.096 0 0 1-1.492.619c-.563 0-1.093-.22-1.493-.62l-8.102-8.06h19.19ZM1.406 18.042V5.959l6.077 6.045-6.077 6.038Zm1 .99 6.074-6.037 1.034 1.03A3.493 3.493 0 0 0 12 15.053c.939 0 1.822-.366 2.485-1.029l1.035-1.03 6.074 6.036H2.406Zm20.188-.99-6.077-6.038 6.077-6.045v12.083Z"></path>
                                        </svg>
                                    </a>
                                    <a target="_blank" class="nl-social2" href="https://www.facebook.com/Symbolab/" data-v-b3dea1e9>
                                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="nuxt-icon" aria-label="Facebook" data-v-b3dea1e9>
                                            <path fill="#DB3F59" d="M13.859 24V13.053h3.673l.55-4.267H13.86V6.062c0-1.235.341-2.077 2.114-2.077l2.258-.001V.167c-.39-.05-1.73-.167-3.29-.167-3.258 0-5.488 1.988-5.488 5.64v3.146H5.769v4.267h3.684V24h4.406Z"></path>
                                        </svg>
                                    </a>
                                    <a target="_blank" class="nl-social2" href="https://twitter.com/symbolab" data-v-b3dea1e9>
                                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="nuxt-icon" aria-label="Twitter" data-v-b3dea1e9>
                                            <g clip-path="url(#i288461827__a)">
                                                <path fill="#DB3F59" d="M24 4.559c-.892.391-1.843.65-2.835.776a4.893 4.893 0 0 0 2.165-2.719 9.833 9.833 0 0 1-3.12 1.191 4.919 4.919 0 0 0-8.511 3.365c0 .39.033.764.114 1.121-4.091-.199-7.71-2.16-10.142-5.146a4.954 4.954 0 0 0-.673 2.487c0 1.704.877 3.214 2.185 4.089A4.859 4.859 0 0 1 .96 9.117v.054a4.943 4.943 0 0 0 3.942 4.835c-.4.109-.837.162-1.29.162a4.35 4.35 0 0 1-.932-.084c.638 1.948 2.447 3.38 4.598 3.427a9.886 9.886 0 0 1-6.1 2.099c-.404 0-.791-.018-1.178-.068a13.852 13.852 0 0 0 7.548 2.208c9.054 0 14.004-7.5 14.004-14.001 0-.217-.008-.427-.018-.636A9.816 9.816 0 0 0 24 4.559Z"></path>
                                            </g>
                                            <defs>
                                                <clipPath id="i288461827__a">
                                                    <path fill="#fff" d="M0 0h24v24H0z"></path>
                                                </clipPath>
                                            </defs>
                                        </svg>
                                    </a>
                                    <a target="_blank" class="nl-social2" href="https://www.instagram.com/symbolab_app/" data-v-b3dea1e9>
                                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="nuxt-icon" aria-label="Instagram" data-v-b3dea1e9>
                                            <g fill="#DB3F59" clip-path="url(#i-60048574__a)">
                                                <path d="M23.977 7.056c-.057-1.275-.263-2.152-.558-2.912a5.857 5.857 0 0 0-1.388-2.128A5.907 5.907 0 0 0 19.907.633C19.143.338 18.27.13 16.995.075 15.711.015 15.303 0 12.046 0 8.785 0 8.377.014 7.097.07 5.823.127 4.946.333 4.187.628a5.856 5.856 0 0 0-2.129 1.388A5.909 5.909 0 0 0 .675 4.14C.38 4.904.173 5.776.117 7.05.057 8.336.042 8.744.042 12.002c0 3.259.014 3.667.07 4.947.057 1.275.263 2.151.559 2.911a5.919 5.919 0 0 0 1.387 2.129c.6.61 1.327 1.083 2.124 1.383.764.295 1.636.501 2.912.558 1.28.056 1.687.07 4.946.07 3.258 0 3.666-.014 4.946-.07 1.275-.057 2.152-.263 2.912-.558a6.139 6.139 0 0 0 3.511-3.512c.296-.764.502-1.636.558-2.911.056-1.28.07-1.688.07-4.947 0-3.258-.004-3.666-.06-4.946Zm-2.162 9.799c-.051 1.172-.248 1.805-.412 2.227a3.981 3.981 0 0 1-2.279 2.278c-.422.165-1.06.361-2.227.413-1.266.056-1.645.07-4.848.07-3.202 0-3.586-.014-4.848-.07-1.172-.052-1.805-.248-2.227-.413a3.693 3.693 0 0 1-1.378-.895 3.73 3.73 0 0 1-.896-1.378c-.164-.422-.36-1.06-.412-2.227-.056-1.266-.07-1.646-.07-4.848 0-3.203.014-3.587.07-4.848.051-1.172.248-1.805.412-2.227.193-.52.497-.994.9-1.379a3.726 3.726 0 0 1 1.38-.895c.421-.164 1.059-.36 2.226-.413 1.266-.056 1.646-.07 4.848-.07 3.207 0 3.586.014 4.848.07 1.172.052 1.805.249 2.227.413.52.192.994.497 1.378.895.399.39.703.858.896 1.379.164.422.36 1.06.412 2.227.056 1.266.07 1.645.07 4.848 0 3.202-.014 3.577-.07 4.843Z"></path>
                                                <path d="M12.044 5.837a6.167 6.167 0 0 0-6.165 6.165 6.167 6.167 0 0 0 6.165 6.166 6.167 6.167 0 0 0 6.166-6.166 6.167 6.167 0 0 0-6.166-6.165Zm0 10.165a4 4 0 1 1 .002-8 4 4 0 0 1-.002 8ZM19.893 5.593a1.44 1.44 0 1 1-2.879 0 1.44 1.44 0 0 1 2.879 0Z"></path>
                                            </g>
                                            <defs>
                                                <clipPath id="i-60048574__a">
                                                    <path fill="#fff" d="M0 0h24v24H0z"></path>
                                                </clipPath>
                                            </defs>
                                        </svg>
                                    </a>
                                </div>
                            </div>
                        </nav>
                    </div>
                    <div id="footer-bottom" data-v-b3dea1e9>
                        <div id="copyright" data-v-b3dea1e9>
                            <div data-v-b3dea1e9>Symbolab, a Learneo, Inc. business</div>
                            <div data-v-b3dea1e9>© Learneo, Inc. 2024</div>
                        </div>
                    </div>
                    <!---->
                    <!---->
                </div>
            </div>
        </div>
        <div id="teleports"></div>
        <script data-cfasync="false" src="/cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script>
        <script type="application/json" data-nuxt-data="nuxt-app" data-ssr="true" id="__NUXT_DATA__">
            [
                [
                    "ShallowReactive",
                    1
                ],
                {
                    "data": 2,
                    "state": 203,
                    "once": 206,
                    "_errors": 207,
                    "serverRendered": 13,
                    "path": 210,
                    "pinia": 211
                },
                [
                    "ShallowReactive",
                    3
                ],
                {
                    "vdBSzZtZfm": 4,
                    "5lJu9mfheh": 7,
                    "cNnjVK40xI": 75,
                    "X0XR7LNWZR": 161
                },
                {
                    "signedIn": 5,
                    "subscribed": 5,
                    "settings": 6,
                    "hasPassword": 5
                },
                false,
                {
                    "printGraph": 5
                },
                [
                    8,
                    14,
                    19,
                    24,
                    29,
                    34,
                    39,
                    44,
                    50,
                    55,
                    60,
                    65,
                    70
                ],
                {
                    "display": 9,
                    "domain": 10,
                    "name": 9,
                    "code": 11,
                    "hreflang": 11,
                    "URL": 12,
                    "provideHrefLang": 13
                },
                "English",
                "www",
                "en",
                "https://www.symbolab.com/popular-algebra/algebra-106",
                true,
                {
                    "display": 15,
                    "domain": 16,
                    "name": 17,
                    "code": 16,
                    "hreflang": 16,
                    "URL": 18,
                    "provideHrefLang": 13
                },
                "Español",
                "es",
                "Spanish",
                "https://es.symbolab.com/popular-algebra/algebra-106",
                {
                    "display": 20,
                    "domain": 21,
                    "name": 22,
                    "code": 21,
                    "hreflang": 21,
                    "URL": 23,
                    "provideHrefLang": 5
                },
                "Português",
                "pt",
                "Portuguese",
                "https://pt.symbolab.com/popular-algebra/algebra-106",
                {
                    "display": 25,
                    "domain": 26,
                    "name": 27,
                    "code": 26,
                    "hreflang": 26,
                    "URL": 28,
                    "provideHrefLang": 5
                },
                "Français",
                "fr",
                "French",
                "https://fr.symbolab.com/popular-algebra/algebra-106",
                {
                    "display": 30,
                    "domain": 31,
                    "name": 32,
                    "code": 31,
                    "hreflang": 31,
                    "URL": 33,
                    "provideHrefLang": 5
                },
                "Deutsch",
                "de",
                "German",
                "https://de.symbolab.com/popular-algebra/algebra-106",
                {
                    "display": 35,
                    "domain": 36,
                    "name": 37,
                    "code": 36,
                    "hreflang": 36,
                    "URL": 38,
                    "provideHrefLang": 5
                },
                "Italiano",
                "it",
                "Italian",
                "https://it.symbolab.com/popular-algebra/algebra-106",
                {
                    "display": 40,
                    "domain": 41,
                    "name": 42,
                    "code": 41,
                    "hreflang": 41,
                    "URL": 43,
                    "provideHrefLang": 5
                },
                "Русский",
                "ru",
                "Russian",
                "https://ru.symbolab.com/popular-algebra/algebra-106",
                {
                    "display": 45,
                    "domain": 46,
                    "name": 47,
                    "code": 46,
                    "hreflang": 48,
                    "URL": 49,
                    "provideHrefLang": 5
                },
                "中文(简体)",
                "zs",
                "Chinese",
                "zh",
                "https://zs.symbolab.com/popular-algebra/algebra-106",
                {
                    "display": 51,
                    "domain": 52,
                    "name": 53,
                    "code": 52,
                    "hreflang": 52,
                    "URL": 54,
                    "provideHrefLang": 5
                },
                "한국어",
                "ko",
                "Korean",
                "https://ko.symbolab.com/popular-algebra/algebra-106",
                {
                    "display": 56,
                    "domain": 57,
                    "name": 58,
                    "code": 57,
                    "hreflang": 57,
                    "URL": 59,
                    "provideHrefLang": 5
                },
                "日本語",
                "ja",
                "Japanese",
                "https://ja.symbolab.com/popular-algebra/algebra-106",
                {
                    "display": 61,
                    "domain": 62,
                    "name": 63,
                    "code": 62,
                    "hreflang": 62,
                    "URL": 64,
                    "provideHrefLang": 5
                },
                "Tiếng Việt",
                "vi",
                "Vietnamese",
                "https://vi.symbolab.com/popular-algebra/algebra-106",
                {
                    "display": 66,
                    "domain": 67,
                    "name": 68,
                    "code": 67,
                    "hreflang": 67,
                    "URL": 69,
                    "provideHrefLang": 5
                },
                "עברית",
                "he",
                "Hebrew",
                "https://he.symbolab.com/popular-algebra/algebra-106",
                {
                    "display": 71,
                    "domain": 72,
                    "name": 73,
                    "code": 72,
                    "hreflang": 72,
                    "URL": 74,
                    "provideHrefLang": 5
                },
                "العربية",
                "ar",
                "Arabic",
                "https://ar.symbolab.com/popular-algebra/algebra-106",
                {
                    "query": 76,
                    "display": 77,
                    "faqs": 78,
                    "solution": 87,
                    "examples": 137,
                    "description": 159,
                    "microdata": 160
                },
                "simplify $$169^{-\\frac{1}{2}}$$",
                "simplify 169^{-1/2}",
                {
                    "ldJson": 79,
                    "problemLatex": 80,
                    "solutionLatex": 81,
                    "problemStr": 77,
                    "solutionStr": 82,
                    "faqs": 83
                },
                "{\n  \"@context\": \"https://schema.org\",\n  \"@type\": \"FAQPage\",\n  \"mainEntity\": [\n  {\n    \"@type\": \"Question\",\n    \"name\": \"What is 169^{-1/2} ?\",\n    \"acceptedAnswer\": {\n      \"@type\": \"Answer\",\n      \"text\": \"The solution to 169^{-1/2} is 1/13\"\n    }\n  }]\n}\n",
                "simplify 169^{-\\frac{1}{2}}",
                "\\frac{1}{13}",
                "1/13",
                [
                    84
                ],
                {
                    "fst": 85,
                    "snd": 86
                },
                "What is 169^{-1/2} ?",
                "The solution to 169^{-1/2} is 1/13",
                {
                    "query": 88,
                    "solution": 90,
                    "steps": 96,
                    "meta": 136
                },
                {
                    "display": 76,
                    "symbolab_question": 89
                },
                "SIMPLIFY#simplify 169^{-\\frac{1}{2}}",
                {
                    "level": 91,
                    "subject": 92,
                    "topic": 92,
                    "subTopic": 93,
                    "default": 81,
                    "decimal": 94,
                    "meta": 95
                },
                "PERFORMED",
                "Algebra",
                "Simplify",
                "0.07692…",
                {
                    "showVerify": 13
                },
                {
                    "type": 97,
                    "title": 98,
                    "input": 99,
                    "steps": 100,
                    "meta": 134
                },
                "interim",
                "$$169^{-\\frac{1}{2}}=\\frac{1}{13}$$",
                "169^{-\\frac{1}{2}}",
                [
                    101,
                    105,
                    108,
                    124,
                    126
                ],
                {
                    "type": 102,
                    "primary": 103,
                    "result": 104
                },
                "step",
                "Factor the number:  $$169=13^{2}$$",
                "=\\left(13^{2}\\right)^{-\\frac{1}{2}}",
                {
                    "type": 102,
                    "primary": 106,
                    "result": 107
                },
                "Apply exponent rule: $$\\left(a^{b}\\right)^{c}=a^{bc},\\:\\quad\\:a\\ge0$$",
                "=13^{2\\left(-\\frac{1}{2}\\right)}",
                {
                    "type": 97,
                    "title": 109,
                    "input": 110,
                    "steps": 111,
                    "meta": 121
                },
                "$$2\\left(-\\frac{1}{2}\\right)=-1$$",
                "2\\left(-\\frac{1}{2}\\right)",
                [
                    112,
                    115,
                    118
                ],
                {
                    "type": 102,
                    "primary": 113,
                    "result": 114
                },
                "Remove parentheses: $$\\left(-a\\right)=-a$$",
                "=-2\\cdot\\:\\frac{1}{2}",
                {
                    "type": 102,
                    "primary": 116,
                    "result": 117
                },
                "Multiply fractions: $$a\\cdot\\frac{b}{c}=\\frac{a\\:\\cdot\\:b}{c}$$",
                "=-\\frac{1\\cdot\\:2}{2}",
                {
                    "type": 102,
                    "primary": 119,
                    "result": 120
                },
                "Cancel the common factor: $$2$$",
                "=-1",
                {
                    "solvingClass": 122,
                    "interimType": 122,
                    "gptData": 123
                },
                "Solver",
                "jypQO0p3kHr3NcERaKKL2kmQGCOF1G+BFP4/DcBVMavLTwR0lYg9k8KUBed0Me102af7LHJT75+lAQkNodor8zm7KvL3CfOtrQj3r5nFTGl2DHrU3TMu6yUg8UPJ84khnlR50gHBSUn7IPRJKVxk1F2rcv3sKP/KpMrHeZi2TdQ6I1ndGJHlQ/YbXY4twSvj7g6EMPsBkt7IKG62imD4IilN5hq+oV3V+IjQvu6ao8K+tcMjKx9YP4Ke6pARsr4wAAAhO6hGUl6O00e+lo6/xJ1uof7d/znJLmVo84V6ifY+rKe1bPNZBFExh8UGPmEF0OTIbJIUp0PP5IQwSvpz1qtJlew0RoCBF/h7gmS1J4qb80RXCLj+seLsPfh0gkVvbHXBvzXPwRh9Priy/MUuRn+voUoRoKC3U1NG/gs7dky9gA226P3IFqnKvFUZQPS1L1Oo2s/DH+KfbvEteLNASOM2mGKW3JDIEEDxnH/KALJZtEHWL2CVSdCGXs0kQfTKfcL/y955bg2pm/pDfToa/mLlG1t/l1PZo8uPSHpIOl9z/pDxMNouLvAim30MXKGMegQT2M4BOfiGMGDdi+Vsd7N9T1hMqhxaJYs3PgPbRkL1xsksDSfLnH3MwmGThJ5GTtlI03/y9U4oXABULCeLnCTYEGk4/KobGwSJ8mxma/1cMgmps8zVNMTqFa1vhzAkTQ+mdPK3AjSJttju60IIPaOI2T2CFPLQPadqQrFTPgcNQwCt9lUx2BCK0uK8JCyizjHDTap7dolkpuqB6uJjSCCfSZGz59qTWoh7fVAoqiozEd9E+sTCP7pC22blY0Y84OtTFravu5rQRjC/ssgl3huNZIXavfLH3Z/Xqh86SBTw/4yUoky0cWU9TjjUfilvcYxerBVP7pM4qoBOWG7o7eAIl1fTgtaFP7RNKlTUGu0gJ/ZZA32ZInFBpDtxBfiKYsrz9VDWKDGWUjCZIeN4sQ==",
                {
                    "type": 102,
                    "result": 125
                },
                "=13^{-1}",
                {
                    "type": 102,
                    "primary": 127,
                    "secondary": 128,
                    "result": 130,
                    "meta": 131
                },
                "Apply exponent rule: $$a^{-1}=\\frac{1}{a}$$",
                [
                    129
                ],
                "$$13^{-1}=\\frac{1}{13}$$",
                "=\\frac{1}{13}",
                {
                    "practiceLink": 132,
                    "practiceTopic": 133
                },
                "/practice/exponent-practice",
                "Expand FOIL",
                {
                    "solvingClass": 135
                },
                "Solver2",
                {
                    "showVerify": 13
                },
                [
                    138,
                    143,
                    147,
                    151,
                    155
                ],
                {
                    "subject": 139,
                    "id": 140,
                    "display": 141,
                    "question": 142
                },
                "algebra",
                "algebra-107",
                "factor 3x^3+27x",
                "factor $$3x^{3}+27x$$",
                {
                    "subject": 139,
                    "id": 144,
                    "display": 145,
                    "question": 146
                },
                "algebra-108",
                "simplify 7/4*2",
                "simplify $$\\frac{7}{4}\\cdot\\:2$$",
                {
                    "subject": 139,
                    "id": 148,
                    "display": 149,
                    "question": 150
                },
                "algebra-109",
                "|4y-3|>=-9",
                "$$\\left|4y-3\\right|\\ge\\:-9$$",
                {
                    "subject": 139,
                    "id": 152,
                    "display": 153,
                    "question": 154
                },
                "algebra-110",
                "3x-x^2>0",
                "$$3x-x^{2}>0$$",
                {
                    "subject": 139,
                    "id": 156,
                    "display": 157,
                    "question": 158
                },
                "algebra-111",
                "simplify sqrt(40)",
                "simplify $$\\sqrt{40}$$",
                "Detailed step by step solution for simplify 169^{-1/2}",
                "{\n  \"@context\": \"https://schema.org\",\n  \"@type\": \"BreadcrumbList\",\n  \"itemListElement\": [\n  {\n    \"@type\": \"ListItem\",\n    \"position\": 1,\n    \"name\": \"Popular Problems\",\n    \"item\": \"https://www.symbolab.com/popular-algebra\"\n  },\n  {\n    \"@type\": \"ListItem\",\n    \"position\": 2,\n    \"name\": \"problem\",\n    \"item\": \"https://www.symbolab.com/popular-algebra/algebra-106\"\n  }]\n}\n",
                [
                    162,
                    165,
                    167,
                    170,
                    173,
                    176,
                    179,
                    182,
                    185,
                    188,
                    191,
                    194,
                    197,
                    200
                ],
                {
                    "url": 163,
                    "translatedTitle": 164
                },
                "pre-algebra-calculator",
                "Pre Algebra",
                {
                    "url": 166,
                    "translatedTitle": 92
                },
                "algebra-calculator",
                {
                    "url": 168,
                    "translatedTitle": 169
                },
                "pre-calculus-calculator",
                "Pre Calculus",
                {
                    "url": 171,
                    "translatedTitle": 172
                },
                "calculus-calculator",
                "Calculus",
                {
                    "url": 174,
                    "translatedTitle": 175
                },
                "functions-line-calculator",
                "Functions",
                {
                    "url": 177,
                    "translatedTitle": 178
                },
                "linear-algebra-calculator",
                "Linear Algebra",
                {
                    "url": 180,
                    "translatedTitle": 181
                },
                "matrix-vector-calculator",
                "Matrices & Vectors",
                {
                    "url": 183,
                    "translatedTitle": 184
                },
                "trigonometry-calculator",
                "Trigonometry",
                {
                    "url": 186,
                    "translatedTitle": 187
                },
                "statistics-calculator",
                "Statistics",
                {
                    "url": 189,
                    "translatedTitle": 190
                },
                "physics-calculator",
                "Physics",
                {
                    "url": 192,
                    "translatedTitle": 193
                },
                "chemistry-calculator",
                "Chemistry",
                {
                    "url": 195,
                    "translatedTitle": 196
                },
                "finance-calculator",
                "Finance",
                {
                    "url": 198,
                    "translatedTitle": 199
                },
                "economics-calculator",
                "Economics",
                {
                    "url": 201,
                    "translatedTitle": 202
                },
                "conversion-calculator",
                "Conversions",
                [
                    "Reactive",
                    204
                ],
                {
                    "$snuxt-i18n-meta": 205
                },
                {
                },
                [
                    "Set"
                ],
                [
                    "ShallowReactive",
                    208
                ],
                {
                    "vdBSzZtZfm": 209,
                    "5lJu9mfheh": 209,
                    "cNnjVK40xI": 209,
                    "X0XR7LNWZR": 209
                },
                null,
                "/popular-algebra/algebra-106",
                {
                    "language": 212,
                    "user": 219,
                    "variation": 234,
                    "layout": 237
                },
                {
                    "selectedLanguage": 213,
                    "siteOrigin": 216,
                    "langPreferenceCookie": 218
                },
                [
                    "Ref",
                    214
                ],
                [
                    "Reactive",
                    215
                ],
                {
                    "code": 11,
                    "display": 9,
                    "subDomain": 10
                },
                [
                    "Ref",
                    217
                ],
                "symbolab.com",
                [
                    "Ref",
                    11
                ],
                {
                    "signingIn": 220,
                    "signedIn": 222,
                    "subscribed": 223,
                    "name": 224,
                    "firstName": 226,
                    "lastName": 227,
                    "udid": 228,
                    "avatarBase64": 229,
                    "avatarStockChoice": 230,
                    "settings": 231,
                    "hasPassword": 233
                },
                [
                    "EmptyRef",
                    221
                ],
                "false",
                [
                    "EmptyRef",
                    221
                ],
                [
                    "EmptyRef",
                    221
                ],
                [
                    "EmptyRef",
                    225
                ],
                "_",
                [
                    "EmptyRef",
                    225
                ],
                [
                    "EmptyRef",
                    225
                ],
                [
                    "EmptyRef",
                    225
                ],
                [
                    "EmptyRef",
                    225
                ],
                [
                    "EmptyRef",
                    225
                ],
                [
                    "Ref",
                    232
                ],
                [
                    "Reactive",
                    6
                ],
                [
                    "EmptyRef",
                    221
                ],
                {
                    "variation": 235
                },
                [
                    "Ref",
                    236
                ],
                3,
                {
                    "showFooter": 238
                },
                [
                    "EmptyRef",
                    221
                ]
            ]</script>
        <script>
            window.__NUXT__ = {};
            window.__NUXT__.config = {
                public: {
                    amplitudeNew: {
                        appKey: "9ec2dedd4eaecd13301a290007705a72"
                    },
                    stripe: {
                        public_key: "pk_live_51K9cHcDlQC6NjZSGnkrAdJB1rOHSZZLt7E4iKZ5US65pgQXPWRWZhxmGsHaK72v9CveqI2d15H8LrAVs0L8FQy2D00Y3fJOz8U"
                    },
                    device: {
                        defaultUserAgent: "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.39 Safari/537.36",
                        enabled: true,
                        refreshOnResize: false
                    },
                    i18n: {
                        baseUrl: "",
                        defaultLocale: "en",
                        defaultDirection: "ltr",
                        strategy: "no_prefix",
                        lazy: true,
                        rootRedirect: "",
                        routesNameSeparator: "___",
                        defaultLocaleRouteNameSuffix: "default",
                        skipSettingLocaleOnNavigate: false,
                        differentDomains: false,
                        trailingSlash: false,
                        locales: [{
                            code: "en",
                            files: ["/root/vue/i18n/en.i18n.ts"]
                        }, {
                            code: "es",
                            files: ["/root/vue/i18n/es.i18n.ts"]
                        }, {
                            code: "pt",
                            files: ["/root/vue/i18n/pt.i18n.ts"]
                        }, {
                            code: "fr",
                            files: ["/root/vue/i18n/fr.i18n.ts"]
                        }, {
                            code: "de",
                            files: ["/root/vue/i18n/de.i18n.ts"]
                        }, {
                            code: "it",
                            files: ["/root/vue/i18n/it.i18n.ts"]
                        }, {
                            code: "ru",
                            files: ["/root/vue/i18n/ru.i18n.ts"]
                        }, {
                            code: "zs",
                            files: ["/root/vue/i18n/zs.i18n.ts"]
                        }, {
                            code: "ko",
                            files: ["/root/vue/i18n/ko.i18n.ts"]
                        }, {
                            code: "ja",
                            files: ["/root/vue/i18n/ja.i18n.ts"]
                        }, {
                            code: "vi",
                            files: ["/root/vue/i18n/vi.i18n.ts"]
                        }, {
                            code: "he",
                            files: ["/root/vue/i18n/he.i18n.ts"]
                        }, {
                            code: "ar",
                            files: ["/root/vue/i18n/ar.i18n.ts"]
                        }],
                        detectBrowserLanguage: false,
                        experimental: {
                            localeDetector: "",
                            switchLocalePathLinkSSR: false,
                            autoImportTranslationFunctions: false,
                            typedPages: true,
                            typedOptionsAndMessages: false,
                            generatedLocaleFilePathFormat: "absolute"
                        },
                        multiDomainLocales: false
                    }
                },
                app: {
                    baseURL: "/",
                    buildId: "79b7348f-b68f-479e-a645-7e898cc571ab",
                    buildAssetsDir: "/_nuxt/",
                    cdnURL: ""
                }
            }
        </script>
    </body>
</html>
"""  # 这里放入你的 HTML 内容

# 解析 HTML
soup = BeautifulSoup(html_content, 'html.parser')

# 提取 JSON 数据
script_tag = soup.find('script', {'id': '__NUXT_DATA__'})
if script_tag:
    script_tag_string = str(script_tag.string)

    # 打印 JSON 数据以调试
    print("提取的 JSON 数据:", script_tag_string)

    try:
        json_data = json.loads(script_tag_string, strict=False)

        # 提取问题、答案和步骤
        problem_latex = json_data[0][1]  # 问题的 LaTeX 格式
        solution_latex = json_data[1][1]  # 答案的 LaTeX 格式
        steps_latex = [step[1] for step in json_data[2][1]]  # 步骤的 LaTeX 格式

        # 输出结果
        print("问题的 LaTeX 格式:", problem_latex)
        print("答案的 LaTeX 格式:", solution_latex)
        print("步骤的 LaTeX 格式:")
        for step in steps_latex:
            print(step)
    except json.JSONDecodeError as e:
        print("JSON 解析错误:", e)
else:
    print("未找到包含问题和答案的 JSON 数据。")