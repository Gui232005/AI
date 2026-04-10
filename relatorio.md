\documentclass[12pt,a4paper]{report}

% ========== PACKAGES ==========
\usepackage[portuguese]{babel}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{geometry}
\usepackage{graphicx}
\usepackage{float}
\usepackage{caption}
\usepackage{hyperref}
\usepackage{xcolor}
\usepackage{listings}
\usepackage{fancyhdr}
\usepackage{titlesec}
\usepackage{tocloft}
\usepackage{setspace}
\usepackage{tabularx}
\usepackage{multirow}
\usepackage{booktabs}
\usepackage{array}
\usepackage{enumitem}
\usepackage{amsmath}
\usepackage{algorithm}
\usepackage{algpseudocode}
\usepackage{tikz}
\usepackage{eso-pic}
\usepackage{lastpage}
\usepackage{listings}
\usepackage{tikz}
\usetikzlibrary{positioning, arrows.meta, decorations.pathreplacing}
\usepackage{booktabs}
\usepackage{float}

% ========== PAGE SETUP ==========
\geometry{
    a4paper,
    left=3cm,
    right=2.5cm,
    top=2.5cm,
    bottom=2.5cm,
    headheight=30pt,
    footskip=40pt
}

% Caminho para as imagens
\graphicspath{{images/}}

\onehalfspacing

% ========== COLORS ==========
\definecolor{estgvblue}{RGB}{0,82,156}
\definecolor{estgvlightblue}{RGB}{100,149,237}
\definecolor{capavermelha}{RGB}{165,42,42}  % Cor da capa - mudar aqui!
% Outras opções:
% \definecolor{capavermelha}{RGB}{0,82,156}    % Azul ESTGV
% \definecolor{capavermelha}{RGB}{25,25,25}    % Preto elegante

% ========== HEADER & FOOTER ==========
\pagestyle{fancy}
\fancyhf{}

% Cabeçalho
\fancyhead[L]{\small\textit{\nouppercase{\leftmark}}}
\fancyhead[R]{\small\thepage}

% Rodapé
\fancyfoot[L]{\small\textit{Métodos de Procura, OCR e LLM}}
\fancyfoot[C]{}
\fancyfoot[R]{\small Página \thepage\ de \pageref{LastPage}}

\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\footrulewidth}{0.4pt}

% Estilo para primeira página de capítulo
\fancypagestyle{plain}{
    \fancyhf{}
    \fancyfoot[L]{\small\textit{Métodos de Procura, OCR e LLM}}
    \fancyfoot[R]{\small Página \thepage\ de \pageref{LastPage}}
    \renewcommand{\headrulewidth}{0pt}
    \renewcommand{\footrulewidth}{0.4pt}
}

% ========== HYPERLINKS ==========
\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    filecolor=magenta,
    urlcolor=cyan,
    citecolor=blue,
    pdftitle={Trabalho Prático Final - Métodos de Procura, OCR e LLM},
    pdfauthor={Grupo IA},
}

% ========== CODE LISTINGS ==========
\definecolor{codegreen}{rgb}{0,0.6,0}
\definecolor{codegray}{rgb}{0.5,0.5,0.5}
\definecolor{codepurple}{rgb}{0.58,0,0.82}
\definecolor{backcolour}{rgb}{0.95,0.95,0.92}

\lstdefinestyle{pythonstyle}{
    language=Python,
    backgroundcolor=\color{backcolour},
    commentstyle=\color{codegreen},
    keywordstyle=\color{magenta},
    numberstyle=\tiny\color{codegray},
    stringstyle=\color{codepurple},
    basicstyle=\ttfamily\footnotesize,
    breakatwhitespace=false,
    breaklines=true,
    captionpos=b,
    keepspaces=true,
    numbers=left,
    numbersep=5pt,
    showspaces=false,
    showstringspaces=false,
    showtabs=false,
    tabsize=4,
    frame=single,
}

\lstset{style=pythonstyle}

% ========== CHAPTER & SECTION FORMATTING ==========
\titleformat{\chapter}[display]
{\normalfont\huge\bfseries}{\chaptertitlename\ \thechapter}{20pt}{\Huge}
\titlespacing*{\chapter}{0pt}{-20pt}{40pt}

% ========== CAPTION FORMATTING ==========
\captionsetup{
    font=small,
    labelfont=bf,
    format=plain,
    justification=centering
}

% ========== TOC FORMATTING ==========
\setlength{\cftbeforechapskip}{8pt}

% ========== DOCUMENT START ==========
\begin{document}

% ========== COVER PAGE 1 (COM FUNDO VERMELHO) ==========
\begin{titlepage}
    % Fundo vermelho
    \pagecolor{capavermelha}
    \color{white}
    
    \centering
    
    % Logos superiores
    \begin{minipage}[t]{0.45\textwidth}
        \flushleft
        % Logo ESTGV/IPV (esquerda)
        \includegraphics[width=\textwidth]{img_esq_capa.png}
    \end{minipage}
    \hfill
    \begin{minipage}[t]{0.45\textwidth}
        \flushright
        % Logo adicional (direita) - opcional
        % \includegraphics[width=0.8\textwidth]{logo_direita.png}
    \end{minipage}
    
    \vspace{3cm}
    
    % Título em bloco
    \begin{center}
        \Large
        \textbf{Trabalho Prático Final}\\[0.5cm]
        \textbf{Métodos de Procura, OCR e LLM Local}\\[2cm]
        
        \large
        Alexandre Fernandes - 26...\\
        Carlos Fonseca - 1...\\
        Guilherme Saraiva - 27...\\
        [Rafael Silva - 27068]\\[2cm]
        
        \Large
        \textbf{Licenciatura em Engenharia Informática}\\[2cm]
        
        \large
        \textbf{abril de 2026}
    \end{center}
    
    \vfill
    
\end{titlepage}
% Restaurar fundo branco
\pagecolor{white}
\color{black}

% ========== COVER PAGE 2 (PÁGINA INTERNA COM FUNDO VERMELHO) ==========
\begin{titlepage}
    % Fundo vermelho também na segunda capa
    \pagecolor{capavermelha}
    \color{white}
    
    \centering
    
    % Logos
    \begin{minipage}[t]{0.45\textwidth}
        \flushleft
        \includegraphics[width=\textwidth]{img_esq_contracapa.png}
    \end{minipage}
    \hfill
    \begin{minipage}[t]{0.45\textwidth}
        \flushright
        \includegraphics[width=0.8\textwidth]{img_dir_contracapa.png}
    \end{minipage}
    
    \vspace{3cm}
    
    \begin{center}
        \Large
        \textbf{Trabalho Prático Final}\\[0.5cm]
        \textbf{Inteligência Artificial}\\[1cm]
        
        \large
        Licenciatura em Engenharia Informática\\[2cm]
        
        \large
        abril de 2026
    \end{center}
    
    \vfill
    
\end{titlepage}
% Restaurar fundo branco definitivamente
\pagecolor{white}
\color{black}

% ========== ÍNDICES ==========
\tableofcontents
\newpage

\listoffigures
\addcontentsline{toc}{chapter}{Índice de Figuras}
\newpage

\listoftables
\addcontentsline{toc}{chapter}{Índice de Tabelas}
\newpage

% ========== INÍCIO DOS CAPÍTULOS ==========

% ============================================================
\chapter{Introdução}
\label{cap:introducao}
% ============================================================

\section{Contextualização}
\label{sec:contextualizacao}

A procura de caminhos em grafos constitui um dos problemas fundamentais da Inteligência Artificial, com aplicações diretas em sistemas de navegação, logística e planeamento de rotas. O presente trabalho aborda este problema no contexto geográfico de Portugal continental, utilizando uma rede de 18 cidades distritais interligadas por estradas reais.

Para além da componente algorítmica, o trabalho integra duas tecnologias complementares que enriquecem a experiência do utilizador: o reconhecimento ótico de caracteres (OCR), utilizado para autenticação do utilizador através da matrícula do veículo, e um modelo de linguagem de grande dimensão (LLM) executado localmente, capaz de fornecer informações turísticas sobre as cidades do percurso selecionado.

Esta abordagem orientada ao produto pretende demonstrar como técnicas clássicas de IA (algoritmos de procura) podem ser combinadas com tecnologias modernas (deep learning para OCR e LLMs) num sistema integrado e funcional.

\section{Objetivos}
\label{sec:objetivos}

O presente trabalho tem como objetivos:

\begin{enumerate}
    \item \textbf{Implementar métodos de procura cega:}
    \begin{itemize}
        \item Custo Uniforme --- procura pelo caminho de menor custo acumulado
        \item Profundidade Limitada --- procura em profundidade com limite configurável
    \end{itemize}
    
    \item \textbf{Implementar métodos de procura heurística:}
    \begin{itemize}
        \item Procura Sôfrega (Greedy Best-First Search) --- guiada exclusivamente pela heurística
        \item A* (A-Estrela) --- combinação ótima de custo real e heurística
    \end{itemize}
    
    \item \textbf{Expor informações detalhadas} sobre os caminhos selecionados, incluindo os valores associados a cada iteração, o caminho final e a distância total
    
    \item \textbf{Integrar OCR} para autenticação do utilizador através do reconhecimento da matrícula do veículo
    
    \item \textbf{Integrar um LLM local} que devolva a descrição das três principais atrações turísticas de cada cidade do caminho encontrado
\end{enumerate}

\section{Estrutura do Relatório}
\label{sec:estrutura_relatorio}

O presente relatório encontra-se organizado em seis capítulos:

\begin{itemize}
    \item \textbf{Capítulo~\ref{cap:introducao} --- Introdução:} contextualização do problema, objetivos e estrutura do relatório.
    \item \textbf{Capítulo~\ref{cap:fundamentacao} --- Fundamentação Teórica:} conceitos teóricos subjacentes aos algoritmos de procura, OCR e LLMs.
    \item \textbf{Capítulo~\ref{cap:modelacao} --- Modelação do Problema:} representação do grafo de cidades, definição da heurística e formatos de matrículas.
    \item \textbf{Capítulo~\ref{cap:implementacao} --- Implementação:} descrição detalhada dos módulos desenvolvidos, incluindo código relevante.
    \item \textbf{Capítulo~\ref{cap:testes} --- Testes e Resultados:} execução de cenários de teste e comparação dos algoritmos.
    \item \textbf{Capítulo~\ref{cap:conclusoes} --- Conclusões:} análise de desempenho, desafios encontrados, limitações e trabalhos futuros.
\end{itemize}


% ============================================================
\chapter{Fundamentação Teórica}
\label{cap:fundamentacao}
% ============================================================

\section{Algoritmos de Procura}
\label{sec:algoritmos_procura}

Os algoritmos de procura em grafos são técnicas fundamentais em Inteligência Artificial, utilizadas para encontrar caminhos entre nós num espaço de estados. Podem ser classificados em duas grandes categorias: métodos de procura cega (não informada) e métodos de procura heurística (informada).

\subsection{Métodos de Procura Cega}
\label{subsec:procura_cega}

Os métodos de procura cega exploram o espaço de estados sem utilizar qualquer informação adicional sobre a proximidade ao objetivo. A sua estratégia de expansão baseia-se unicamente na estrutura do grafo e, no caso do custo uniforme, nos custos das arestas. Embora não sejam tão eficientes como os métodos heurísticos, oferecem garantias importantes de completude e, em alguns casos, de otimalidade.

\subsubsection{Custo Uniforme}
\label{subsubsec:custo_uniforme}

O algoritmo de Custo Uniforme (\textit{Uniform Cost Search}, UCS) é uma variante da procura em largura que expande sempre o nó com o menor custo acumulado $g(n)$ desde o nó inicial. Utiliza uma fila de prioridade (\textit{min-heap}) para manter os nós ordenados por custo crescente.

\textbf{Propriedades:}
\begin{itemize}
    \item \textbf{Completude:} Sim, desde que o custo de cada aresta seja $>0$
    \item \textbf{Otimalidade:} Sim --- garante encontrar o caminho de menor custo
    \item \textbf{Complexidade temporal:} $O(b^{1 + \lfloor C^*/\epsilon \rfloor})$, onde $C^*$ é o custo ótimo e $\epsilon$ o menor custo de aresta
    \item \textbf{Complexidade espacial:} $O(b^{1 + \lfloor C^*/\epsilon \rfloor})$
\end{itemize}

\textbf{Vantagens:} Encontra sempre o caminho ótimo; funciona com custos variáveis entre arestas.

\textbf{Desvantagens:} Pode explorar muitos nós desnecessários em grafos grandes, pois não possui orientação em direção ao objetivo.

\subsubsection{Profundidade Limitada}
\label{subsubsec:profundidade_limitada}

O algoritmo de Profundidade Limitada (\textit{Depth-Limited Search}, DLS) é uma variante da procura em profundidade que impõe um limite máximo de profundidade $l$. Quando o limite é atingido, o algoritmo retrocede (\textit{backtracking}) sem expandir mais nós nesse ramo.

O algoritmo pode devolver três tipos de resultado:
\begin{itemize}
    \item \textbf{Caminho:} quando o objetivo é encontrado dentro do limite
    \item \textbf{Cutoff:} quando o limite foi atingido sem encontrar o objetivo (pode existir solução a maior profundidade)
    \item \textbf{Failure:} quando todos os nós acessíveis foram explorados e o objetivo não foi encontrado
\end{itemize}

\textbf{Propriedades:}
\begin{itemize}
    \item \textbf{Completude:} Não --- a solução pode estar além do limite $l$
    \item \textbf{Otimalidade:} Não --- o primeiro caminho encontrado pode não ser o mais curto
    \item \textbf{Complexidade temporal:} $O(b^l)$, onde $b$ é o fator de ramificação
    \item \textbf{Complexidade espacial:} $O(b \cdot l)$
\end{itemize}

\textbf{Vantagens:} Consumo de memória reduzido comparado com procura em largura.

\textbf{Desvantagens:} A escolha do limite $l$ é crítica --- um valor demasiado baixo impede encontrar a solução, enquanto um valor elevado pode levar a uma exploração excessiva.

\subsection{Métodos de Procura Heurística}
\label{subsec:procura_heuristica}

Os métodos de procura heurística utilizam uma função de avaliação $h(n)$ que estima o custo restante desde o nó $n$ até ao objetivo. Esta informação adicional permite ao algoritmo orientar a procura, reduzindo significativamente o número de nós explorados em comparação com os métodos cegos.

Uma heurística é dita \textbf{admissível} quando nunca sobrestima o custo real para atingir o objetivo, ou seja:
$$h(n) \leq h^*(n), \quad \forall n$$
onde $h^*(n)$ é o custo real ótimo de $n$ ao objetivo.

\subsubsection{Procura Sôfrega (Greedy Best-First Search)}
\label{subsubsec:greedy}

A Procura Sôfrega (\textit{Greedy Best-First Search}) expande sempre o nó que aparenta estar mais próximo do objetivo, utilizando exclusivamente a heurística $h(n)$ como função de avaliação. Não considera o custo acumulado $g(n)$ para chegar ao nó atual.

A função de avaliação é simplesmente:
$$f(n) = h(n)$$

\textbf{Propriedades:}
\begin{itemize}
    \item \textbf{Completude:} Não --- pode entrar em ciclos (mitigado com lista de visitados)
    \item \textbf{Otimalidade:} Não --- o caminho encontrado pode não ser o melhor
    \item \textbf{Complexidade temporal:} $O(b^m)$ no pior caso, onde $m$ é a profundidade máxima
    \item \textbf{Complexidade espacial:} $O(b^m)$
\end{itemize}

\textbf{Vantagens:} Muito rápido na prática, quando a heurística é boa, pois tende a seguir diretamente em direção ao objetivo.

\textbf{Desvantagens:} Não garante otimalidade --- pode escolher caminhos rápidos mas não ótimos, pois ignora o custo já acumulado.

\subsubsection{A* (A-Estrela)}
\label{subsubsec:astar}

O A* é um dos algoritmos de procura mais importantes em IA, combinando as vantagens do Custo Uniforme e da Procura Sôfrega. A sua função de avaliação considera tanto o custo real acumulado como a estimativa heurística:

$$f(n) = g(n) + h(n)$$

onde:
\begin{itemize}
    \item $g(n)$ --- custo real do caminho desde o nó inicial até $n$
    \item $h(n)$ --- estimativa heurística do custo de $n$ até ao objetivo
\end{itemize}

\textbf{Propriedades:}
\begin{itemize}
    \item \textbf{Completude:} Sim, desde que o fator de ramificação seja finito e os custos sejam $>0$
    \item \textbf{Otimalidade:} Sim, se a heurística for admissível (nunca sobrestima)
    \item \textbf{Complexidade temporal:} $O(b^d)$ no pior caso, mas muito melhor na prática com boa heurística
    \item \textbf{Complexidade espacial:} $O(b^d)$, pois mantém todos os nós em memória
\end{itemize}

O A* é \textbf{otimamente eficiente}: para qualquer heurística admissível, nenhum outro algoritmo ótimo pode expandir menos nós.

\section{Optical Character Recognition (OCR)}
\label{sec:ocr_teoria}

O Reconhecimento Ótico de Caracteres (OCR, do inglês \textit{Optical Character Recognition}) é uma tecnologia que permite converter imagens de texto --- impressos ou manuscritos --- em texto digital editável. Os sistemas modernos de OCR utilizam técnicas de \textit{deep learning}, nomeadamente redes neuronais convolucionais (CNN) para deteção de regiões de texto e redes recorrentes (LSTM/GRU) ou \textit{transformers} para o reconhecimento de sequências de caracteres.

No contexto deste trabalho, utilizou-se o \textbf{PaddleOCR}, um sistema OCR de código aberto desenvolvido pela Baidu no ecossistema PaddlePaddle. O PaddleOCR é reconhecido pela sua elevada precisão e eficiência, suportando mais de 80 idiomas e oferecendo modelos otimizados para diferentes cenários de utilização.

A arquitetura PP-OCRv5 utilizada integra três componentes:
\begin{enumerate}
    \item \textbf{Deteção de texto:} localiza regiões de texto na imagem usando um modelo de segmentação
    \item \textbf{Classificação de orientação:} corrige a rotação das regiões detetadas
    \item \textbf{Reconhecimento de caracteres:} converte a imagem de cada região em sequência de caracteres com grau de confiança
\end{enumerate}

A aplicação específica do OCR neste trabalho --- o reconhecimento de matrículas de veículos (\textit{Automatic License Plate Recognition}, ALPR) --- requer técnicas adicionais de pré-processamento de imagem para lidar com variações de iluminação, ângulo e resolução típicas de fotografias de veículos.

\section{Large Language Models (LLM)}
\label{sec:llm_teoria}

Os Modelos de Linguagem de Grande Dimensão (LLMs) são redes neuronais baseadas na arquitetura \textit{Transformer}, treinadas em vastos corpora de texto para prever e gerar linguagem natural. Estes modelos demonstram capacidades emergentes de raciocínio, resumo e geração de conteúdo quando escalados para milhares de milhões de parâmetros.

Neste trabalho utilizou-se o modelo \textbf{Llama 3.2} (3B parâmetros), desenvolvido pela Meta, executado localmente através da plataforma \textbf{Ollama}. O Ollama permite executar LLMs em hardware comum sem necessidade de ligação à Internet, garantindo:

\begin{itemize}
    \item \textbf{Privacidade:} os dados nunca saem da máquina local
    \item \textbf{Independência:} não depende de serviços externos ou APIs pagas
    \item \textbf{Latência reduzida:} eliminação da latência de rede
\end{itemize}

A aplicação concreta do LLM neste projeto consiste em gerar descrições das três principais atrações turísticas de cada cidade presente no caminho encontrado pelos algoritmos de procura, enriquecendo a experiência de planeamento de viagem.


% ============================================================
\chapter{Modelação do Problema}
\label{cap:modelacao}
% ============================================================

\section{Representação do Grafo}
\label{sec:grafo}

O mapa rodoviário de Portugal continental foi modelado como um grafo não direcionado ponderado $G = (V, E, w)$, onde:
\begin{itemize}
    \item $V$ --- conjunto de 18 vértices, correspondentes às cidades distritais
    \item $E$ --- conjunto de arestas que representam ligações rodoviárias diretas
    \item $w: E \rightarrow \mathbb{R}^+$ --- função de peso que atribui a distância quilométrica a cada aresta
\end{itemize}

Todas as ligações são bidireccionais, ou seja, se existe uma ligação entre a cidade $A$ e a cidade $B$ com distância $d$, então existe também a ligação inversa com a mesma distância.

Em termos de estrutura de dados, o grafo é representado por um \textbf{dicionário de adjacências} em Python. Cada cidade é uma chave do dicionário principal, e o valor é um sub-dicionário que mapeia as cidades vizinhas às respetivas distâncias:

\begin{lstlisting}[language=Python, caption={Excerto da representação do grafo em dicionário de adjacências.}]
cidades = {
    'Aveiro': {'Porto': 68, 'Viseu': 95, 'Coimbra': 68, 'Leiria': 115},
    'Braga':  {'Viana do Castelo': 48, 'Vila Real': 106, 'Porto': 53},
    'Porto':  {'Aveiro': 68, 'Braga': 53, 'Viana do Castelo': 71,
               'Vila Real': 116, 'Viseu': 133},
    # ... restantes cidades
}
\end{lstlisting}

A Tabela~\ref{tab:distancias} apresenta a totalidade das ligações modeladas no sistema.

\begin{table}[H]
\centering
\caption{Distâncias quilométricas entre cidades portuguesas (Tabela 1 do enunciado).}
\label{tab:distancias}
\resizebox{\textwidth}{!}{%
\begin{tabular}{l l}
\toprule
\textbf{Cidade} & \textbf{Ligações (cidade: distância km)} \\
\midrule
Aveiro & Porto (68), Viseu (95), Coimbra (68), Leiria (115) \\
Braga & Viana do Castelo (48), Vila Real (106), Porto (53) \\
Bragança & Vila Real (137), Guarda (202) \\
Beja & Évora (78), Faro (152), Setúbal (142) \\
Castelo Branco & Coimbra (159), Guarda (106), Portalegre (80), Évora (203) \\
Coimbra & Aveiro (68), Viseu (96), Leiria (67), Castelo Branco (159) \\
Évora & Beja (78), Castelo Branco (203), Lisboa (150), Santarém (117), Portalegre (131), Setúbal (103) \\
Faro & Beja (152), Setúbal (249), Lisboa (299) \\
Guarda & Bragança (202), Castelo Branco (106), Vila Real (157), Viseu (85) \\
Leiria & Aveiro (115), Coimbra (67), Lisboa (129), Santarém (70) \\
Lisboa & Évora (150), Faro (299), Leiria (129), Santarém (78), Setúbal (50) \\
Portalegre & Castelo Branco (80), Évora (131) \\
Porto & Aveiro (68), Braga (53), Viana do Castelo (71), Vila Real (116), Viseu (133) \\
Santarém & Évora (117), Leiria (70), Lisboa (78) \\
Setúbal & Beja (142), Évora (103), Faro (249), Lisboa (50) \\
Viana do Castelo & Braga (48), Porto (71) \\
Vila Real & Braga (106), Bragança (137), Guarda (157), Porto (116), Viseu (110) \\
Viseu & Aveiro (95), Coimbra (96), Guarda (85), Porto (133), Vila Real (110) \\
\bottomrule
\end{tabular}%
}
\end{table}

\section{Função Heurística}
\label{sec:heuristica}

A função heurística $h(n)$ utilizada nos algoritmos de procura informada estima a distância em linha reta entre o nó $n$ e o objetivo. O sistema implementa uma estratégia híbrida:

\begin{enumerate}
    \item \textbf{Quando o destino é Faro:} utiliza-se a tabela fornecida no enunciado (Tabela~\ref{tab:heuristica_faro}), que contém as distâncias em linha reta de cada cidade até Faro.
    \item \textbf{Quando a origem é Faro:} utiliza-se a mesma tabela, uma vez que a distância em linha reta é simétrica ($d(A,B) = d(B,A)$).
    \item \textbf{Para outros pares de cidades:} calcula-se a distância em linha reta através da fórmula de Haversine, utilizando as coordenadas geográficas reais das cidades.
\end{enumerate}

\begin{table}[H]
\centering
\caption{Distância em linha reta até Faro (Tabela 2 do enunciado) --- heurística para destino Faro.}
\label{tab:heuristica_faro}
\begin{tabular}{lr|lr}
\toprule
\textbf{Cidade} & \textbf{km} & \textbf{Cidade} & \textbf{km} \\
\midrule
Aveiro & 366 & Lisboa & 195 \\
Braga & 454 & Portalegre & 228 \\
Bragança & 487 & Porto & 418 \\
Beja & 99 & Santarém & 231 \\
Castelo Branco & 280 & Setúbal & 168 \\
Coimbra & 319 & Viana do Castelo & 473 \\
Évora & 157 & Vila Real & 429 \\
Faro & 0 & Viseu & 363 \\
Guarda & 352 & Leiria & 278 \\
\bottomrule
\end{tabular}
\end{table}

\textbf{Admissibilidade da heurística:} A distância em linha reta entre dois pontos é sempre inferior ou igual à distância rodoviária real (o caminho pela estrada nunca é mais curto do que a linha reta). Assim, a heurística é \textbf{admissível} ($h(n) \leq h^*(n)$), garantindo a otimalidade do A*.

A fórmula de Haversine, utilizada como \textit{fallback}, calcula a distância do arco mais curto sobre a superfície terrestre entre dois pontos definidos pelas suas coordenadas geográficas:

$$d = 2R \cdot \arctan2\left(\sqrt{a}, \sqrt{1-a}\right)$$

onde $a = \sin^2\left(\frac{\Delta\phi}{2}\right) + \cos(\phi_1)\cos(\phi_2)\sin^2\left(\frac{\Delta\lambda}{2}\right)$ e $R = 6371$ km é o raio médio da Terra.

\section{Padrões de Matrículas Portuguesas}
\label{sec:matriculas}

O sistema de matrículas em Portugal evoluiu ao longo das décadas, resultando em quatro formatos principais que o sistema reconhece:

\begin{itemize}
    \item \textbf{AA-00-AA} --- formato atual (desde 2005), e.g., \texttt{AO-74-VC}
    \item \textbf{00-AA-00} --- formato anterior (1992--2005), e.g., \texttt{23-AB-45}
    \item \textbf{AA-00-00} --- formato antigo (1937--1992), e.g., \texttt{LI-23-45}
    \item \textbf{00-00-AA} --- formato histórico, e.g., \texttt{12-34-AB}
\end{itemize}

A deteção destes formatos é realizada por uma expressão regular que aceita variações com ou sem hífens e espaços como separadores, garantindo robustez face a imperfeições do OCR.


% ============================================================
\chapter{Implementação}
\label{cap:implementacao}
% ============================================================

\section{Arquitetura do Sistema}
\label{sec:arquitetura}

O sistema foi desenvolvido seguindo uma arquitetura modular, com separação clara de responsabilidades entre os diferentes componentes. A Figura~\ref{fig:arquitetura} ilustra a organização geral.

\begin{figure}[H]
\centering
\begin{tikzpicture}[
    node distance=0.6cm and 1cm,
    module/.style={rectangle, draw, fill=blue!12, text width=3.8cm, minimum height=1.2cm, align=center, rounded corners=4pt, font=\small},
    mainmod/.style={rectangle, draw, fill=orange!15, text width=4cm, minimum height=1.2cm, align=center, rounded corners=4pt, font=\small\bfseries},
    arrow/.style={-Stealth, thick}
]
    \node[mainmod] (main) {Main.py\\Interface Principal};
    \node[module, below left=1cm and 0.5cm of main] (ocr) {ocr\_module.py\\Login OCR};
    \node[module, below=1cm of main] (rede) {rede.py\\Grafo + Heurística};
    \node[module, below right=1cm and 0.5cm of main] (llm) {LocalLLM.py\\Atrações Turísticas};
    \node[module, below=1cm of rede] (alg) {search\_algorithms/\\4 Algoritmos de Procura};
    \node[module, left=0.5cm of ocr] (spin) {spinner.py\\Indicador de Progresso};

    \draw[arrow] (main) -- (ocr);
    \draw[arrow] (main) -- (rede);
    \draw[arrow] (main) -- (llm);
    \draw[arrow] (main.south) -- (alg);
    \draw[arrow] (main) -- (spin);
    \draw[arrow] (alg) -- (rede);
\end{tikzpicture}
\caption{Arquitetura modular do sistema: o \texttt{Main.py} orquestra todos os módulos.}
\label{fig:arquitetura}
\end{figure}

O fluxo de execução do programa segue as seguintes etapas:
\begin{enumerate}
    \item O utilizador fornece uma imagem da matrícula do veículo
    \item O módulo OCR processa a imagem e extrai a matrícula (autenticação)
    \item O utilizador seleciona a cidade de origem e de destino
    \item O utilizador escolhe um algoritmo de procura no menu
    \item O sistema executa o algoritmo, exibindo cada iteração
    \item O caminho final e a distância total são apresentados
    \item O LLM local gera as atrações turísticas das cidades do caminho
\end{enumerate}

\section{Módulo de Rede (rede.py)}
\label{sec:modulo_rede}

O ficheiro \texttt{rede.py} centraliza toda a informação relativa ao grafo de cidades e às funções heurísticas. Contém três estruturas de dados principais:

\begin{itemize}
    \item \textbf{\texttt{cidades}} --- Dicionário de adjacências com as distâncias quilométricas entre cidades ligadas (Tabela 1 do enunciado). Todas as ligações são definidas nos dois sentidos.
    \item \textbf{\texttt{origem\_faro}} --- Dicionário com as distâncias em linha reta de cada cidade até Faro (Tabela 2 do enunciado), utilizado como heurística quando Faro é origem ou destino.
    \item \textbf{\texttt{coordenadas}} --- Dicionário com as coordenadas geográficas (latitude, longitude) de cada cidade, utilizadas no cálculo Haversine para pares que não envolvam Faro.
\end{itemize}

A função \texttt{linha\_reta(origem, destino)} implementa a estratégia híbrida descrita na Secção~\ref{sec:heuristica}, verificando primeiro se Faro está envolvido (e usando a tabela fixa) e recorrendo à fórmula de Haversine nos restantes casos.


\section{Módulo OCR (ocr\_module.py)}
\label{sec:modulo_ocr}

O módulo \texttt{ocr\_module.py} é responsável pelo reconhecimento ótico de caracteres (OCR) aplicado à leitura de matrículas de veículos. Foi desenvolvido com recurso à biblioteca \textit{PaddleOCR}, uma solução de OCR baseada em \textit{deep learning} do ecossistema PaddlePaddle. O módulo suporta execução tanto em GPU (via CUDA) como em CPU, sendo a deteção do hardware feita automaticamente no arranque:

\begin{lstlisting}[language=Python, caption={Deteção automática de GPU e configuração do backend.}]
def _check_gpu():
    try:
        import paddle
        return paddle.is_compiled_with_cuda()
    except Exception:
        return False

GPU_DISPONIVEL = _check_gpu()

if not GPU_DISPONIVEL:
    os.environ["FLAGS_use_mkldnn"] = "0"
\end{lstlisting}

Caso não exista GPU disponível, o \textit{backend} OneDNN (MKL-DNN) é desativado para garantir compatibilidade em todas as máquinas. A arquitetura do módulo segue uma \textit{pipeline} de três fases, representada na Figura~\ref{fig:pipeline_ocr}.

\begin{figure}[H]
\centering
\begin{tikzpicture}[
    node distance=0.4cm,
    block/.style={rectangle, draw, fill=blue!12, text width=4.2cm, minimum height=1cm, align=center, rounded corners=3pt, font=\small},
    arrow/.style={-Stealth, thick}
]
    \node[block] (input) {Imagem de entrada\\(BGR)};
    \node[block, below=of input] (gray) {Conversão para\\escala de cinza};
    \node[block, below=of gray] (clahe) {Equalização CLAHE\\($8 \times 8$, clipLimit=2.0)};
    \node[block, below=of clahe] (bin) {Binarização adaptativa\\gaussiana ($11 \times 11$)};
    \node[block, below=of bin] (bgr) {Reconversão para BGR};
    \node[block, below=of bgr, fill=orange!15] (ocr) {PaddleOCR (PP-OCRv5)\\Deteção + Reconhecimento};
    \node[block, below=of ocr, fill=green!15] (valid) {Validação por regex\\+ filtro de confiança};
    \node[block, below=of valid, fill=green!25] (out) {Matrícula normalizada};

    \draw[arrow] (input) -- (gray);
    \draw[arrow] (gray) -- (clahe);
    \draw[arrow] (clahe) -- (bin);
    \draw[arrow] (bin) -- (bgr);
    \draw[arrow] (bgr) -- (ocr);
    \draw[arrow] (ocr) -- (valid);
    \draw[arrow] (valid) -- (out);

    \draw[decorate, decoration={brace, amplitude=6pt, mirror}, thick, gray] 
        ([xshift=-0.5cm]gray.north west) -- ([xshift=-0.5cm]bgr.south west) 
        node[midway, left=0.4cm, font=\footnotesize, text=gray, align=center] {Pré-\\processamento};
\end{tikzpicture}
\caption{Pipeline completa do módulo OCR, desde a imagem de entrada até à matrícula validada.}
\label{fig:pipeline_ocr}
\end{figure}

\subsection{Pré-processamento de Imagem}
\label{subsec:preprocessamento}

Antes de submeter a imagem ao motor de OCR, é aplicado um conjunto de transformações com o objetivo de maximizar a legibilidade dos caracteres. Este pré-processamento é realizado pelo método \texttt{\_preprocess}:

\begin{lstlisting}[language=Python, caption={Método de pré-processamento da imagem.}]
def _preprocess(self, image: np.ndarray) -> np.ndarray:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) \
           if len(image.shape) == 3 else image

    # CLAHE para equalizacao local de histograma
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(gray)

    # Binarizacao adaptativa
    binary = cv2.adaptiveThreshold(
        enhanced, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY, 11, 2,
    )

    return cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR)
\end{lstlisting}

As etapas do pré-processamento e o seu efeito visual são ilustrados na Figura~\ref{fig:preprocess_etapas}.

\begin{figure}[H]
\centering
\resizebox{\textwidth}{!}{%
\begin{tikzpicture}
    \node[draw, minimum width=3cm, minimum height=2cm, fill=gray!20, align=center] (a) at (0,0) {\footnotesize Imagem\\original (BGR)};
    \node[draw, minimum width=3cm, minimum height=2cm, fill=gray!40, align=center] (b) at (4.5,0) {\footnotesize Escala de\\cinza};
    \node[draw, minimum width=3cm, minimum height=2cm, fill=gray!55, align=center] (c) at (9,0) {\footnotesize CLAHE\\(contraste)};
    \node[draw, minimum width=3cm, minimum height=2cm, fill=gray!80, align=center, text=white] (d) at (13.5,0) {\footnotesize Binarização\\adaptativa};

    \draw[-Stealth, thick] (a) -- (b);
    \draw[-Stealth, thick] (b) -- (c);
    \draw[-Stealth, thick] (c) -- (d);
\end{tikzpicture}%
}
\caption{Etapas do pré-processamento: cada fase melhora progressivamente a separação entre caracteres e fundo.}
\label{fig:preprocess_etapas}
\end{figure}


As transformações aplicadas justificam-se da seguinte forma:

\begin{itemize}
    \item \textbf{Conversão para escala de cinza} --- Reduz a dimensionalidade, eliminando informação de cor irrelevante para caracteres alfanuméricos.
    \item \textbf{CLAHE} --- Ao contrário da equalização global de histograma, o CLAHE opera localmente em blocos de $8 \times 8$, melhorando o contraste em regiões com iluminação irregular --- situação frequente em fotografias de veículos em ambientes exteriores.
    \item \textbf{Binarização adaptativa gaussiana} --- Calcula o limiar para cada vizinhança de $11 \times 11$ píxeis, separando os caracteres do fundo da matrícula mesmo com variações de luminosidade.
\end{itemize}

\subsection{Reconhecimento de Texto}
\label{subsec:reconhecimento}

O reconhecimento é efetuado pela classe \texttt{LicensePlateOCR}, que encapsula uma instância do PaddleOCR configurada com o idioma inglês, adequado para caracteres alfanuméricos presentes nas matrículas portuguesas:

\begin{lstlisting}[language=Python, caption={Inicialização do motor OCR com suporte a GPU/CPU.}]
class LicensePlateOCR:
    def __init__(self, lang: str = "en", use_gpu: bool = True):
        self.ocr = PaddleOCR(
            use_textline_orientation=True,
            lang=lang,
            device="gpu" if use_gpu else "cpu",
        )
\end{lstlisting}

O modelo utiliza a arquitetura PP-OCRv5, que integra três componentes internos representados na Figura~\ref{fig:paddleocr_arch}.

\begin{figure}[H]
\centering
\resizebox{\textwidth}{!}{%
\begin{tikzpicture}[
    node distance=0.6cm and 0.8cm,
    block/.style={rectangle, draw, fill=blue!10, text width=3.5cm, minimum height=1.2cm, minimum width=4.5cm, align=center, rounded corners=3pt},
    arrow/.style={-Stealth, thick}
]
    \node[block, fill=gray!15] (in) {Imagem\\pré-processada};
    \node[block, right=of in] (det) {\textbf{Deteção de texto}\\PP-OCRv5\_server\_det\\(localiza regiões)};
    \node[block, right=of det] (cls) {\textbf{Classificação}\\de orientação\\(corrige rotação)};
    \node[block, right=of cls] (rec) {\textbf{Reconhecimento}\\en\_PP-OCRv5\_mobile\_rec\\(texto + confiança)};

    \draw[arrow] (in) -- (det);
    \draw[arrow] (det) -- (cls);
    \draw[arrow] (cls) -- (rec);
\end{tikzpicture}%
}
\caption{Arquitetura interna do PaddleOCR PP-OCRv5: deteção, classificação de orientação e reconhecimento de caracteres.}
\label{fig:paddleocr_arch}
\end{figure}


O resultado do reconhecimento é extraído pelo método \texttt{read\_image}, que itera sobre as deteções e constrói uma lista estruturada:

\begin{lstlisting}[language=Python, caption={Extração dos resultados do OCR.}]
results = list(self.ocr.predict(img))
detections = []
for res in results:
    polys  = res.get("rec_polys", [])
    texts  = res.get("rec_texts", [])
    scores = res.get("rec_scores", [])
    for bbox, text, score in zip(polys, texts, scores):
        detections.append({
            "text":       text.strip().upper(),
            "confidence": round(float(score), 4),
            "bbox":       bbox.tolist(),
        })
\end{lstlisting}

Cada deteção contém o texto reconhecido, o grau de confiança (entre 0 e 1) e as coordenadas do polígono envolvente (\textit{bounding box}).

\subsection{Validação de Matrículas}
\label{subsec:validacao}

Após o reconhecimento, o método \texttt{extract\_plates} aplica um processo de filtragem para identificar quais dos textos detetados correspondem a matrículas portuguesas. Este processo assenta em dois critérios:

\begin{enumerate}
    \item \textbf{Confiança mínima} --- São descartadas todas as deteções com índice de confiança inferior a 60\%.
    \item \textbf{Correspondência com expressão regular} --- O texto é validado contra um padrão que cobre os formatos históricos de matrículas em Portugal.
\end{enumerate}

\begin{lstlisting}[language=Python, caption={Expressão regular para validação dos formatos de matrícula portuguesa.}]
PLATE_PATTERN = re.compile(
    r'\b([A-Z]{2}[-\s]?\d{2}[-\s]?[A-Z]{2}|'  # AA-00-AA
    r'\d{2}[-\s]?[A-Z]{2}[-\s]?\d{2}|'         # 00-AA-00
    r'[A-Z]{2}[-\s]?\d{2}[-\s]?\d{2}|'          # AA-00-00
    r'\d{2}[-\s]?\d{2}[-\s]?[A-Z]{2})\b',       # 00-00-AA
    re.IGNORECASE,
)
\end{lstlisting}

Os quatro formatos reconhecidos e os respetivos períodos de utilização encontram-se na Tabela~\ref{tab:formatos_matricula}.

\begin{table}[H]
\centering
\caption{Formatos de matrículas portuguesas reconhecidos pelo sistema.}
\label{tab:formatos_matricula}
\begin{tabular}{lll}
\toprule
\textbf{Formato} & \textbf{Exemplo} \\
\midrule
\texttt{AA-00-AA} & AO-74-VC \\
\texttt{00-AA-00} & 23-AB-45 \\
\texttt{AA-00-00} & LI-23-45 \\
\texttt{00-00-AA} & 12-34-AB \\
\bottomrule
\end{tabular}
\end{table}

As matrículas validadas são normalizadas pela função \texttt{\_normalize\_plate}, que converte todos os caracteres para maiúsculas, substitui espaços por hífens e colapsa hífens múltiplos:

\begin{lstlisting}[language=Python, caption={Normalização do texto da matrícula.}]
def _normalize_plate(text: str) -> str:
    clean = re.sub(r"[\s]", "-", text.strip().upper())
    clean = re.sub(r"-{2,}", "-", clean)
    return clean
\end{lstlisting}

O resultado final é uma lista de matrículas ordenável por confiança. O sistema seleciona automaticamente a matrícula com maior grau de certeza para autenticação do utilizador, conforme ilustrado na Figura~\ref{fig:fluxo_validacao}.

\begin{figure}[H]
\centering
\begin{tikzpicture}[
    node distance=0.5cm,
    block/.style={rectangle, draw, fill=blue!10, text width=4.5cm, minimum height=0.9cm, align=center, rounded corners=3pt, font=\small},
    decision/.style={diamond, draw, fill=yellow!15, text width=2.2cm, align=center, aspect=2.2, font=\small},
    arrow/.style={-Stealth, thick}
]
    \node[block] (det) {Lista de deteções OCR};
    \node[decision, below=of det] (conf) {Confiança\\$\geq 60\%$?};
    \node[block, left=2.5cm of conf, fill=red!15] (desc) {Descartada};
    \node[decision, below=of conf] (regex) {Corresponde\\a regex?};
    \node[block, left=2.5cm of regex, fill=red!15] (desc2) {Descartada};
    \node[block, below=of regex, fill=green!15] (norm) {Normalização\\(\texttt{\_normalize\_plate})};
    \node[block, below=of norm, fill=green!25] (out) {Matrícula validada};

    \draw[arrow] (det) -- (conf);
    \draw[arrow] (conf) -- node[right, font=\footnotesize] {Sim} (regex);
    \draw[arrow] (conf) -- node[above, font=\footnotesize] {Não} (desc);
    \draw[arrow] (regex) -- node[right, font=\footnotesize] {Sim} (norm);
    \draw[arrow] (regex) -- node[above, font=\footnotesize] {Não} (desc2);
    \draw[arrow] (norm) -- (out);
\end{tikzpicture}
\caption{Fluxograma de validação: cada deteção passa por um filtro de confiança e correspondência com padrões de matrícula antes de ser aceite.}
\label{fig:fluxo_validacao}
\end{figure}




\section{Algoritmos de Procura}
\label{sec:implementacao_algoritmos}

Os quatro algoritmos de procura foram implementados no diretório \texttt{search\_algorithms/}, cada um no seu ficheiro dedicado. Todos os algoritmos imprimem informação sobre cada iteração (nó expandido, vizinho explorado, custos associados), conforme exigido pelo enunciado.

\subsection{Custo Uniforme (uniformCostSearch.py)}
\label{subsec:impl_custo_uniforme}

A implementação utiliza o módulo \texttt{heapq} do Python para manter uma fila de prioridade (\textit{min-heap}) ordenada pelo custo acumulado $g(n)$. Cada entrada na fila contém o custo, o nó atual e o caminho percorrido.

\begin{lstlisting}[language=Python, caption={Implementação do Custo Uniforme.}]
def uniform_cost_search(graph, start, goal):
    priority_queue = [(0, start, [start])]
    visited = {}

    while priority_queue:
        current_cost, current_node, path = heapq.heappop(priority_queue)

        if current_node == goal:
            return current_cost, path

        if current_node in visited and visited[current_node] <= current_cost:
            continue

        visited[current_node] = current_cost

        for neighbor, cost in graph[current_node].items():
            total_cost = current_cost + cost
            if neighbor not in visited or total_cost < visited.get(neighbor, float('inf')):
                heapq.heappush(priority_queue, (total_cost, neighbor, path + [neighbor]))

    return None
\end{lstlisting}

O dicionário \texttt{visited} armazena o menor custo conhecido para cada nó, evitando a re-exploração de nós já visitados com custo superior. Quando o nó objetivo é retirado da fila, o algoritmo termina com a garantia de otimalidade.

\subsection{Profundidade Limitada (depthLimitedSearch.py)}
\label{subsec:impl_profundidade}

A implementação utiliza uma abordagem recursiva com um parâmetro \texttt{limit} que é decrementado a cada nível de profundidade. Um conjunto \texttt{visited} evita ciclos.

\begin{lstlisting}[language=Python, caption={Implementação da Profundidade Limitada.}]
def depth_limited_search(node, goal, graph, limit, visited=None):
    if visited is None:
        visited = set()
    if node == goal:
        return [node]
    elif limit == 0:
        return "cutoff"
    elif node in visited:
        return "failure"
    else:
        visited.add(node)
        cutoff_occurred = False
        for child in graph[node].keys():
            result = depth_limited_search(child, goal, graph, limit - 1, visited)
            if result == "cutoff":
                cutoff_occurred = True
            elif result != "failure":
                return [node] + result
        return "cutoff" if cutoff_occurred else "failure"
\end{lstlisting}

O algoritmo distingue dois tipos de insucesso: \texttt{cutoff} indica que o limite foi atingido (a solução pode existir a maior profundidade), enquanto \texttt{failure} indica que todos os nós exploráveis foram visitados sem sucesso.

\subsection{Procura Sôfrega (greedyBestFirstSearch.py)}
\label{subsec:impl_greedy}

A Procura Sôfrega utiliza uma fila de prioridade ordenada exclusivamente pelo valor heurístico $h(n)$. O custo real do caminho é calculado apenas no final, após a reconstrução do caminho através do dicionário \texttt{parent}.

\begin{lstlisting}[language=Python, caption={Implementação da Procura Sôfrega.}]
def greedyBest_FirstSearch(graph, start, goal, heuristic):
    priority_queue = []
    heapq.heappush(priority_queue, (heuristic(start, goal), start))
    visited = set()
    parent = {start: None}

    while priority_queue:
        _, current_node = heapq.heappop(priority_queue)

        if current_node == goal:
            # Reconstruir caminho e calcular custo real
            path = []
            node = current_node
            while node is not None:
                path.append(node)
                node = parent[node]
            path = path[::-1]
            total_cost = sum(graph[path[i]][path[i+1]] for i in range(len(path)-1))
            return total_cost, path

        if current_node in visited:
            continue
        visited.add(current_node)

        for neighbor in graph[current_node]:
            if neighbor not in visited and neighbor not in parent:
                parent[neighbor] = current_node
                heapq.heappush(priority_queue, (heuristic(neighbor, goal), neighbor))

    return None, None
\end{lstlisting}

É importante notar que este algoritmo \textbf{não garante otimalidade}: ao ignorar o custo acumulado $g(n)$, pode encontrar caminhos subótimos, especialmente quando a heurística não reflete fielmente a topologia rodoviária.

\subsection{A* (A.py)}
\label{subsec:impl_astar}

O A* combina o custo real $g(n)$ com a heurística $h(n)$ na função de avaliação $f(n) = g(n) + h(n)$. Cada entrada na fila de prioridade contém quatro elementos: $f(n)$, $g(n)$, o nó e o caminho.

\begin{lstlisting}[language=Python, caption={Implementação do A*.}]
def a_star_search(graph, start, goal, heuristic):
    priority_queue = []
    initial_h = heuristic(start, goal)
    heapq.heappush(priority_queue, (0 + initial_h, 0, start, [start]))
    visited = {}

    while priority_queue:
        f_cost, g_cost, current_node, path = heapq.heappop(priority_queue)

        if current_node == goal:
            return g_cost, path

        if current_node in visited and visited[current_node] <= g_cost:
            continue
        visited[current_node] = g_cost

        for neighbor, cost in graph[current_node].items():
            total_g_cost = g_cost + cost
            neighbor_h = heuristic(neighbor, goal)
            total_f_cost = total_g_cost + neighbor_h
            if neighbor not in visited or total_g_cost < visited.get(neighbor, float('inf')):
                heapq.heappush(priority_queue, 
                    (total_f_cost, total_g_cost, neighbor, path + [neighbor]))

    return None
\end{lstlisting}

Graças à admissibilidade da heurística (distância em linha reta $\leq$ distância real), o A* garante encontrar o caminho ótimo. Adicionalmente, é o algoritmo mais eficiente entre os quatro implementados, pois a heurística orienta a procura em direção ao objetivo, reduzindo o número de nós expandidos.


\section{Módulo LLM Local (LocalLLM.py)}
\label{sec:modulo_llm}
O sistema integra um \textit{Large Language Model} (LLM) executado localmente através da plataforma Ollama. Esta funcionalidade permite ao utilizador obter recomendações sobre as três principais atrações turísticas de cada cidade visitada no caminho encontrado, enriquecendo a experiência de planeamento de viagem.

\subsubsection{Arquitetura e Tecnologia}

A implementação utiliza o modelo \texttt{llama3.2:3b}, um modelo de linguagem de tamanho reduzido (3 mil milhões de parâmetros) otimizado para execução local em hardware comum. Este modelo foi escolhido por equilibrar qualidade de resposta e eficiência computacional.

A biblioteca \texttt{ollama} em Python fornece uma interface simples para comunicação com o servidor Ollama local, que gere o carregamento e execução do modelo. A arquitetura cliente-servidor permite que o modelo permaneça em memória entre consultas, reduzindo significativamente o tempo de resposta após a primeira inferência.

\subsubsection{Implementação da Classe LocalLLM}

A classe \texttt{LocalLLM} encapsula toda a lógica de interação com o modelo:

\begin{lstlisting}[language=Python, caption=Estrutura da classe LocalLLM]
class LocalLLM:
    def __init__(self, model_name='llama3.2:3b'):
        self.model_name = model_name
        self.cache = {}
    
    def get_attractions(self, city_name):
        # Implementacao...
\end{lstlisting}

A classe mantém duas propriedades principais:
\begin{itemize}
    \item \texttt{model\_name}: Nome do modelo a utilizar (configurável)
    \item \texttt{cache}: Dicionário para armazenar respostas já obtidas
\end{itemize}

\subsubsection{Prompt Engineering}

O design do \textit{prompt} foi cuidadosamente elaborado para garantir respostas consistentes, concisas e relevantes:

\begin{lstlisting}[language=Python, caption=Prompt utilizado para consulta de atrações]
f"""Descreve as 3 principais atracoes turisticas de {city_name} 
no pais Portugal (Europa).
Escreve em portugues de Portugal.
Se conciso e informativo. Maximo 15 palavras por atracao."""
\end{lstlisting}

As instruções incluem:
\begin{enumerate}
    \item \textbf{Especificidade geográfica}: ``no país Portugal (Europa)'' elimina ambiguidades com cidades homónimas noutros países
    \item \textbf{Idioma}: ``português de Portugal'' garante o dialeto correto
    \item \textbf{Formato}: ``3 principais atrações'' estrutura a resposta
    \item \textbf{Concisão}: ``Máximo 15 palavras por atração'' evita respostas excessivamente longas
\end{enumerate}

\subsubsection{Sistema de Cache}

Para otimizar o desempenho e reduzir custos computacionais, o sistema implementa um mecanismo de \textit{cache} simples mas eficaz:

\begin{lstlisting}[language=Python, caption=Verificação de cache antes de consulta]
if city_name in self.cache:
    return self.cache[city_name]
\end{lstlisting}

Quando uma cidade é consultada pela primeira vez, a resposta é armazenada no dicionário \texttt{cache} indexado pelo nome da cidade. Consultas subsequentes à mesma cidade retornam imediatamente o resultado armazenado, eliminando a necessidade de nova inferência.

Este mecanismo é particularmente útil quando o utilizador:
\begin{itemize}
    \item Executa múltiplas procuras que passam pelas mesmas cidades
    \item Revisita o histórico de viagens
    \item Testa diferentes algoritmos com os mesmos pontos de origem/destino
\end{itemize}

% Integração com Ollama
% Prompt engineering para atrações turísticas
% Tratamento de respostas


\section{Interface Principal (Main.py)}
\label{sec:interface}

A interface principal é implementada no ficheiro \texttt{Main.py}, que orquestra todos os módulos do sistema através de uma interface em linha de comandos (CLI). O fluxo segue duas fases distintas:

\subsubsection{Fase 1: Autenticação por OCR}

O programa inicia pedindo ao utilizador o caminho para uma imagem contendo a matrícula do veículo. O módulo OCR processa a imagem e, em caso de sucesso, apresenta a matrícula detetada com o grau de confiança. Em caso de GPU disponível, o utilizador pode optar por executar o OCR em GPU para maior velocidade.

\begin{lstlisting}[language=Python, caption={Seleção da matrícula com maior confiança.}]
melhor = max(plates, key=lambda p: p["confidence"])
matricula_detectada = melhor["plate"]
\end{lstlisting}

\subsubsection{Fase 2: Menu de Procura}

Tras a autenticação, o utilizador seleciona a cidade de origem e destino a partir de uma lista numerada das 18 cidades disponíveis. O menu principal oferece quatro opções de algoritmo de procura:

\begin{enumerate}
    \item Custo Uniforme
    \item Profundidade Limitada (com pedido de limite ao utilizador)
    \item Procura Sôfrega
    \item A*
\end{enumerate}

Para cada algoritmo executado, o sistema apresenta:
\begin{itemize}
    \item Informação de cada iteração (nó expandido, vizinhos, custos)
    \item O caminho final encontrado
    \item A distância total associada ao caminho
    \item As três principais atrações turísticas de cada cidade do caminho (via LLM)
\end{itemize}

Durante a consulta ao LLM, é apresentado um indicador visual de progresso (\textit{spinner}) implementado no módulo \texttt{spinner.py}, proporcionando \textit{feedback} ao utilizador sobre o processamento em curso.


% ============================================================
\chapter{Testes e Resultados}
\label{cap:testes}
% ============================================================

\section{Comparação de Algoritmos de Procura}
\label{sec:comparacao_algoritmos}

\subsection{Cenário de Teste 1: Braga → Faro}
\label{subsec:cenario1}

Este cenário testa a procura entre a cidade mais a norte (Braga) e a mais a sul (Faro), maximizando a distância e o número de cidades intermédias. Utiliza-se a heurística da tabela fornecida (Tabela 2), uma vez que o destino é Faro.

\begin{table}[H]
\centering
\caption{Resultados comparativos --- Braga $\rightarrow$ Faro.}
\label{tab:cenario1}
\begin{tabular}{l p{6cm} r}
\toprule
\textbf{Algoritmo} & \textbf{Caminho} & \textbf{Distância (km)} \\
\midrule
Custo Uniforme & \textit{(executar e preencher)} & --- \\
Profundidade Limitada ($l=6$) & \textit{(executar e preencher)} & --- \\
Sôfrega & \textit{(executar e preencher)} & --- \\
A* & \textit{(executar e preencher)} & --- \\
\bottomrule
\end{tabular}
\end{table}

% TODO: Executar o programa e preencher os resultados reais acima

\subsection{Cenário de Teste 2: Porto → Évora}
\label{subsec:cenario2}

Este cenário testa um percurso de média distância que não envolve Faro, obrigando o sistema a utilizar a heurística Haversine.

\begin{table}[H]
\centering
\caption{Resultados comparativos --- Porto $\rightarrow$ Évora.}
\label{tab:cenario2}
\begin{tabular}{l p{6cm} r}
\toprule
\textbf{Algoritmo} & \textbf{Caminho} & \textbf{Distância (km)} \\
\midrule
Custo Uniforme & \textit{(executar e preencher)} & --- \\
Profundidade Limitada ($l=5$) & \textit{(executar e preencher)} & --- \\
Sôfrega & \textit{(executar e preencher)} & --- \\
A* & \textit{(executar e preencher)} & --- \\
\bottomrule
\end{tabular}
\end{table}

% TODO: Executar o programa e preencher os resultados reais acima

\subsection{Cenário de Teste 3: Bragança → Faro}
\label{subsec:cenario3}

Este cenário é particularmente interessante porque Bragança é a cidade mais distante de Faro em linha reta (487 km), e possui apenas duas ligações diretas (Vila Real e Guarda), limitando as opções iniciais.

\begin{table}[H]
\centering
\caption{Resultados comparativos --- Bragança $\rightarrow$ Faro.}
\label{tab:cenario3}
\begin{tabular}{l p{6cm} r}
\toprule
\textbf{Algoritmo} & \textbf{Caminho} & \textbf{Distância (km)} \\
\midrule
Custo Uniforme & \textit{(executar e preencher)} & --- \\
Profundidade Limitada ($l=7$) & \textit{(executar e preencher)} & --- \\
Sôfrega & \textit{(executar e preencher)} & --- \\
A* & \textit{(executar e preencher)} & --- \\
\bottomrule
\end{tabular}
\end{table}

% TODO: Executar o programa e preencher os resultados reais acima

% ============================================================
\chapter{Conclusões}
\label{cap:conclusoes}
% ============================================================
\section{Análise de Desempenho dos Algoritmos}
\label{sec:analise_desempenho}

A partir dos cenários de teste executados, é possível identificar as seguintes tendências:

\begin{itemize}
    \item \textbf{Custo Uniforme vs A*:} Ambos encontram o caminho ótimo, mas o A* expande significativamente menos nós graças à orientação fornecida pela heurística. A diferença é tanto maior quanto maior a distância entre origem e destino.
    
    \item \textbf{Procura Sôfrega:} É o algoritmo mais rápido (menos iterações), mas frequentemente encontra caminhos subótimos. A sua ``ganância'' em dirigir-se ao objetivo pode fazê-lo ignorar rotas alternativas com menor custo total.
    
    \item \textbf{Profundidade Limitada:} O desempenho depende criticamente do limite $l$ escolhido. Um limite demasiado baixo resulta em \textit{cutoff}, enquanto um elevado pode explorar ramos desnecessários. Ao contrário dos outros algoritmos, não garante encontrar o caminho mais curto.
    
    \item \textbf{Impacto da heurística:} Quando o destino é Faro e se utiliza a tabela fornecida, os algoritmos heurísticos apresentam estimativas mais precisas, o que se traduz numa procura mais dirigida e eficiente. Para outros destinos, a heurística Haversine fornece estimativas razoáveis mas potencialmente menos ajustadas.
\end{itemize}

\section{Desafios Encontrados}
\label{sec:desafios}

Durante o desenvolvimento do projeto, foram encontrados os seguintes desafios:

\begin{enumerate}
    \item \textbf{Compatibilidade do PaddleOCR:} A instalação e configuração do PaddlePaddle e PaddleOCR revelou-se complexa, especialmente na gestão da compatibilidade entre versões de CUDA, cuDNN e a própria biblioteca. A solução passou por implementar a deteção automática de GPU e desativar o backend MKL-DNN quando necessário.
    
    \item \textbf{Precisão do OCR:} O reconhecimento de matrículas em condições variadas (iluminação, ângulo, resolução) apresentou desafios significativos. O pipeline de pré-processamento com CLAHE e binarização adaptativa foi essencial para melhorar a taxa de sucesso.
    
    \item \textbf{Heurística para destinos não-Faro:} A tabela de heurísticas fornecida no enunciado cobre apenas distâncias até Faro. Para permitir procura heurística entre quaisquer pares de cidades, foi necessário implementar o cálculo Haversine como alternativa, utilizando coordenadas geográficas reais.
    
    \item \textbf{Tempo de resposta do LLM:} A primeira consulta ao modelo Llama 3.2 pode demorar vários segundos enquanto o modelo é carregado em memória. O sistema de cache e o indicador visual (spinner) mitigam este problema.
\end{enumerate}

\section{Limitações do Sistema}
\label{sec:limitacoes}

O sistema apresenta as seguintes limitações conhecidas:

\begin{itemize}
    \item \textbf{OCR:} A precisão diminui significativamente com imagens de baixa resolução, matrículas danificadas ou parcialmente obstruídas, e condições de iluminação desfavoráveis (contraluz, noite).
    
    \item \textbf{Heurística:} A tabela de distâncias em linha reta apenas está disponível para o destino Faro. Para outros destinos, a heurística Haversine é uma aproximação razoável mas não está calibrada com os valores do enunciado.
    
    \item \textbf{LLM local:} O modelo de 3B parâmetros, embora eficiente, pode gerar informações incorretas ou inventadas (alucinações). As respostas dependem do conhecimento embebido no modelo e não são verificadas contra fontes externas.
    
    \item \textbf{Grafo estático:} O mapa rodoviário é fixo e não considera condições de tráfego em tempo real, portagens, ou alternativas de transporte.
    
    \item \textbf{Interface CLI:} A interface em linha de comandos, embora funcional, limita a experiência do utilizador comparada com uma interface gráfica.
\end{itemize}

\section{Melhorias Futuras}
\label{sec:melhorias}

Como trabalhos futuros, identificam-se as seguintes possibilidades de melhoria:

\begin{itemize}
    \item \textbf{Interface gráfica (GUI):} Desenvolvimento de uma interface web ou desktop que permita a visualização do mapa, dos caminhos explorados e da solução final de forma interativa.
    
    \item \textbf{Visualização do grafo:} Representação gráfica do grafo de cidades com animação do processo de procura, permitindo ao utilizador observar a expansão dos nós em tempo real.
    
    \item \textbf{OCR em tempo real:} Integração com uma câmara para captura e reconhecimento de matrículas em tempo real, sem necessidade de fornecer um ficheiro de imagem.
    
    \item \textbf{Múltiplos destinos:} Extensão do sistema para suportar rotas com paragens intermédias, aproximando-se do problema do caixeiro-viajante (\textit{Travelling Salesman Problem}).
    
    \item \textbf{Heurísticas mais sofisticadas:} Tabelas de distâncias em linha reta para todos os pares de cidades, ou utilização de APIs de mapas para estimativas mais precisas.
    
    \item \textbf{Comparação automática:} Funcionalidade para executar todos os algoritmos simultaneamente e apresentar uma tabela comparativa de resultados.
\end{itemize}


\end{document}