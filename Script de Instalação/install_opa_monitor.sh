#!/bin/bash

# Caminho da pasta compartilhada
SHARED_PATH="/home/sirius/shared/gop-services/gop-monitor"

# 1. Garantir permissões de execução
chmod +x "$SHARED_PATH/OPA-Monitor.bash"
chmod +x "$SHARED_PATH/OPA-Monitor.desktop"

# 2. Copiar o .desktop para a área de trabalho do usuário
cp "$SHARED_PATH/OPA-Monitor.desktop" ~/Desktop/

# 3. Copiar o ícone para a área de trabalho (opcional)
cp "$SHARED_PATH/icon.png" ~/Desktop/ 2>/dev/null

# 4. Mensagem final
echo "Instalação concluída. Vá até a área de trabalho, clique com o botão direito no ícone OPA-Monitor e selecione 'Permitir execução como programa'."
0

