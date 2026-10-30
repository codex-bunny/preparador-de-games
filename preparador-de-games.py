import time
import subprocess
print('olá, isso é um projeto pessoal meu que tenta fazer a instalação das coisas nessesaria para jogar no linux seja mais tranquila.')
print('irei fazer algumas perguntas basicas para a instalação, primeiro, qual é a sua gpu? suporte apenas a amd, intel e nvidia por enquanto')
print('qual a sua gpu?')
gpu = input().strip().lower() 

# pacotes das gpus e dos games (por distro)

pacote_amd_arch = ['mesa', 'vulkan-radeon', 'lib32-mesa', 'lib32-vulkan-radeon', 'linux-firmware-amdgpu']
pacote_amd_debian = ['mesa-vulkan-drivers', 'libgl1-mesa-dri', 'libglx-mesa0', 'firmware-amd-graphics']
pacote_amd_fedora = ['mesa-dri-drivers', 'mesa-vulkan-drivers', 'mesa-va-drivers', 'linux-firmware']
pacote_intel_arch = ['mesa', 'vulkan-intel', 'intel-media-driver', 'libva', 'intel-gpu-tools']
pacote_intel_debian = ['mesa-vulkan-drivers', 'libgl1-mesa-dri', 'intel-media-va-driver', 'libva2', 'intel-gpu-tools']
pacote_intel_fedora = ['mesa-dri-drivers', 'mesa-vulkan-drivers', 'intel-media-driver', 'libva', 'intel-gpu-tools']
pacote_nvidia_arch = ['mesa', 'nvidia', 'nvidia-prime', 'nvidia-utils', 'lib32-nvidia-utils', 'vulkan-icd-loader']
pacote_nvidia_debian = ['nvidia-driver', 'nvidia-vulkan-icd', 'libglx-mesa0']
pacote_nvidia_fedora = ['akmod-nvidia', 'xorg-x11-drv-nvidia', 'xorg-x11-drv-nvidia-libs']
pacote_games_arch = ['wine', 'heroic', 'steam', 'dxvk', 'mangohud']
pacote_games_debian = ['wine', 'steam-installer', 'dxvk', 'mangohud']
pacote_games_fedora = ['wine', 'steam', 'dxvk', 'mangohud']
pacote_sem_gpu = []
gerenciador_de_pacotes = input('Qual gerenciador de pacotes você utiliza? ').strip().lower()

# instalação pacman

if gerenciador_de_pacotes == "pacman":
    if gpu == 'amd':
        print('Você ira baixando mesa, vulkan-radeon, lib32-mesa, lib32-vulkan-radeon, linux-firmware-amdgpu, steam, wine, dxvk e mangohud')
        pacotes_amd_arch = pacote_amd_arch + pacote_games_arch
    elif gpu == 'nvidia':
        print('Você ira baixando mesa, nvidia, nvidia-prime, nvidia utils, lib32-nvidia-utils e vulkan-icd-loader')
        pacotes_nvidia_arch = pacote_nvidia_arch + pacote_games_arch
    elif gpu == 'intel':
        print('Você ira baixando mesa, vulkan-intel, intel-media-driver, libva, intel-gpu-tools')
        pacotes_intel_arch = pacote_intel_arch + pacote_games_arch
    else:
        print('gpu não reconhecida, você ira baixar apenas as dependencias que não tem ligamento com a gpu, sendo elas steam, wine, dxvk e mangohub, o heroic será futuramente implementado, eu enfrento problemas por causa da instalação via flatpak dele')
        pacotes_sem_gpu = pacote_sem_gpu + pacote_games_arch
    elif pacotes_amd_arch:
        if gpu == 'amd':
            resultadu = input('Você tem certeza? [s ou n] ')
            if resultadu.strip().lower() in ['s', 'sim']:
                resultado = subprocess.run(
                    ['pacman', '-S', '--needed', *pacotes_amd_arch],
                    text=True
                )
            print(f'Código de saída: {resultado.returncode}')
        else:
            print('Instalação cancelada.')
    elif pacotes_nvidia_arch:
        if gpu == 'nvidia':
            resultadu = input('Você tem certeza? [s ou n] ')
            if resultadu.strip().lower() in ['s', 'sim']:
                resultado = subprocess.run(
                    ['pacman', '-S', '--needed', *pacotes_nvidia_arch],
                    text=True
                )
            print(f'Código de saída: {resultado.returncode}')
        else:
            print('Instalação cancelada.')
    elif pacotes_intel_arch:
        if gpu == 'intel':
            resultadu = input('Você tem certeza? [s ou n] ')
            if resultadu.strip().lower() in ['s', 'sim']:
                resultado = subprocess.run(
                    ['pacman', '-S', '--needed', *pacotes_intel_arch],
                    text=True
                )
            print(f'Código de saída: {resultado.returncode}')
        else:
            print('Instalação cancelada.')
    else:
        print('Nenhum pacote selecionado para instalação.')

# instalação apt

elif gerenciador_de_pacotes == "apt":
    if gpu == 'amd':
        print('Você esta baixando mesa, vulkan-radeon, lib32-mesa, lib32-vulkan-radeon, linux-firmware-amdgpu, steam, heroic games launcher, wine, dxvk e mangohud')
        pacotes_amd_debian = pacote_amd_debian + pacote_games_debian
    elif gpu == 'nvidia':
        print('Você esta baixando mesa, nvidia, nvidia-prime, nvidia utils, lib32-nvidia-utils e vulkan-icd-loader')
        pacotes_nvidia_debian = pacote_nvidia_debian + pacote_games_debian
    elif gpu == 'intel':
        print('Você esta baixando mesa, vulkan-intel, intel-media-driver, libva, intel-gpu-tools')
        pacotes_intel_debian = pacote_intel_debian + pacote_games_debian
    else:
        print('gpu não reconhecida')
        pacotes_sem_gpu = pacote_sem_gpu + pacote_games_debian
    if gpu == "amd":
        resultadou = input('Você tem certeza? [s ou n] ')
        if resultadou.strip().lower() in ['s', 'sim']:
            resultadoo = subprocess.run(
                ['apt', 'install', '--no-install-recommends', *pacotes_amd_debian],
                text=True
            )
            print(f'Código de saída: {resultadoo.returncode}')
        else:
            print('Instalação cancelada.')
    elif gpu == "nvidia":
        resultadou = input('Você tem certeza? [s ou n] ')
        if resultadou.strip().lower() in ['s', 'sim']:
            resultadoo = subprocess.run(
                ['apt', 'install', '--no-install-recommends', *pacotes_nvidia_debian],
                text=True
            )
            print(f'Código de saída: {resultadoo.returncode}')
        else:
            print('Instalação cancelada.')
    elif gpu == 'intel':
        resultadou = input('Você tem certeza? [s ou n] ')
        if resultadou.strip().lower() in ['s', 'sim']:
            resultadoo = subprocess.run(
                ['apt', 'install', '--no-install-recommends', *pacotes_intel_debian],
                text=True
            )
            print(f'Código de saída: {resultadoo.returncode}')
        else:
            print('Instalação cancelada.')
    else:
        print('gpu não encontrada, irei instalar apenas os pacotes de jogos')
        resultadou = input('Você tem certeza? [s ou n] ')
        if resultadou.strip().lower() in ['s', 'sim']:
            resultadoo = subprocess.run(
                ['apt', 'install', '--no-install-recommends', *pacotes_sem_gpu],
                text=True
            )
            print(f'Código de saída: {resultadoo.returncode}')
        else:
            print('Instalação cancelada.')
elif gerenciador_de_pacotes == "dnf":
        print("ainda em produção")
elif gerenciador_de_pacotes == "apk":
        print("ainda em produção")
# o que esperar e o que não esperar desse projeto
# o que esperar:
# um projeto feito com dedicação e por amor ao open soure
# um projeto feito pensando em pessoas leigas e preguiçosos
# o que NÃO esperar:
# um projeto que ira abranger distros alem de arch, debian, fedora, alpine e suas variantes
# um projeto com GUI, pelo menos o projeto original não tera gui, mas se um dia eu ficar sem fazer nada eu provavelmente faço um fork com gui