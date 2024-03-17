import pytest

from parkmylatex.converter import get_rephrased_doc

def test_get_rephrased_doc():
    text = 
    r"""
    \noindent \\
\textbf{Optimal Allocation for Stratified Sampling.} \textit{Proof of \cref{the:OptimalMarginals}}:
The relaxed sample allocation problem for marginal contributions is given by:
\begin{align*}
    (m_{i,\ell}^*)_{i \in \mathcal{N}, \ell \in \mathcal{L}_{\Delta}'} = \argmin\limits_{(m_{i,\ell})_{i \in \mathcal{N}, \ell \in \mathcal{L}_{\Delta}'}} & \hspace{0.5cm} \frac{1}{n^3} \sum\limits_{i=1}^n \sum\limits_{\ell=1}^{n-2} \frac{\sigma_{i,\ell}^2}{m_{i,\ell}} \\
    \text{s.t.} & \hspace{0.5cm} 2 \sum\limits_{i=1}^n \sum\limits_{\ell=1}^{n-2} m_{i,\ell} = \tilde{T} \\
    & \hspace{0.5cm} m_{i,\ell} \in \mathbb{R}_{>0} \hspace{1.6cm} \forall i \in \mathcal{N}, \ell \in \mathcal{L}_{\Delta}' \, .
\end{align*}
We solve for $\nabla L = 0$ which requires

\begin{equation*}
    \frac{\partial}{\partial m_{i,\ell}} L = - \frac{\sigma_{i,\ell}^2}{n^3 m_{i,\ell}^2} + 2\lambda \stackrel{!}{=} 0 \hspace{0.2cm} \forall i \in \mathcal{N}, \ell \in \mathcal{L}_{\Delta}'
    \hspace{0.3cm} \text{and} \hspace{0.3cm}
    \frac{\partial}{\partial \lambda} L =  2 \sum\limits_{i=1}^n \sum\limits_{\ell=1}^{n-2} m_{i,\ell} - \tilde{T} \stackrel{!}{=} 0 \, .
\end{equation*}


    """
    result = get_rephrased_doc