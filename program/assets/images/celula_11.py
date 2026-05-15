# =========================
# CÉLULA 11 - AVALIAÇÃO DA RNA
# =========================

# Faz previsões usando os dados de teste
y_pred = modelo_rna.predict(X_teste)

# =========================
# MÉTRICAS
# =========================

mae = mean_absolute_error(
    y_teste,
    y_pred
)

rmse = np.sqrt(
    mean_squared_error(
        y_teste,
        y_pred
    )
)

r2 = r2_score(
    y_teste,
    y_pred
)

# Acurácia aproximada
acuracia_aproximada = max(
    0,
    100 - mae
)

# =========================
# RESULTADOS
# =========================

print("=" * 60)
print("AVALIAÇÃO DA REDE NEURAL")
print("=" * 60)

print(f"MAE: {mae:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"R²: {r2:.4f}")
print(f"Acurácia aproximada: {acuracia_aproximada:.2f}%")

# =========================
# GRÁFICO
# =========================

# Seleciona apenas algumas amostras
amostras = 50

plt.figure(figsize=(14, 5))

plt.plot(
    y_teste[:amostras],
    label="Urgência Esperada (Especialista)"
)

plt.plot(
    y_pred[:amostras],
    label="Urgência Prevista pela RNA"
)

plt.title(
    "Comparação entre Sistema Especialista e RNA"
)

plt.ylabel("Urgência (%)")

plt.xlabel("Amostras")

plt.grid(True)

plt.legend()

plt.show()