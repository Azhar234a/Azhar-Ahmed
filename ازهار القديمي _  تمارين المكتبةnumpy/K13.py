plt.bar(k, count[1:], alpha=0.5, label='sample count')
plt.plot(k, n*(k**-a)/zeta(a), 'k.-', alpha=0.5,
label='expected count')
plt.semilogy()
plt.grid(alpha=0.4)
plt.legend()
plt.title(f'Zipf sample, a={a}, size={n}')
plt.show()