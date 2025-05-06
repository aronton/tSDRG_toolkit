#!/bin/bash
#SBATCH --job-name=replace1
#SBATCH --ntasks=replace2
#SBATCH --partition=replace3
#SBATCH --cpus-per-task=1
#SBATCH --output=replace4

source ~/.bashrc

date

FILE=$1
outputPath="replace4"

cd /dicos_ui_home/aronton/tSDRG_random/tSDRG/Main_15
# 讀取 eee 檔案並解析 s1, s2, ds
while IFS=: read -r key value; do
    value=$(echo "$value" | xargs)  # 去除前後空白
    if [[ "$key" == "s1" ]]; then
        s1=$value
    elif [[ "$key" == "s2" ]]; then
        s2=$value
    elif [[ "$key" == "ds" ]]; then
        ds=$value
    fi
done < "$FILE"

echo "parameterfile : $FILE"
echo "The working directory : $PWD"

# 確保變數都有值
if [[ -z "$s1" || -z "$s2" || -z "$ds" ]]; then
    echo "錯誤: s1, s2, ds 讀取失敗！"
    exit 1
fi

# 計算分組數量
cols=$(((s2 - s1 + 1) / ds ))
echo "s1: $s1, s2: $s2, ds: $ds, cols: $cols"
# 定義行數與列數
rows=$ds
# cols=$((s2/ds))
echo
echo -e "$rows"
echo -e "$cols"
# 初始化二維陣列（用一維陣列模擬）
# array=()

# # 填充二維陣列
# for ((i=0; i<rows; i++)); do
#     for ((j=0; j<cols; j++)); do
#         # 計算一維索引
#         index=$((i * cols + j))
#         array[index]=$((i * cols + j + 1))  # 填充數據
#     done
# done

# 輸出二維陣列的內容
for ((i=0; i<cols; i++)); do
    echo "Round${i} start $(date)"
    echo  # 輸出一行
    date
    s1_combine=$((s1 - 1 + i * rows + 1))
    # echo "s1_combine:${s1_combine}"
    for ((j=0; j<rows; j++)); do
        index=$((s1 - 1 + i * rows + j + 1))
        echo "srun --exclusive --nodes=1 --ntasks=1 --cpus-per-task=1 ./spin15try.exe ${FILE} ${index} ${index} &"
        srun --exclusive --nodes=1 --ntasks=1 --cpus-per-task=1 ./spin15try.exe ${FILE} ${index} ${index} &
    done
    s2_combine=$((s1 - 1 + (i+1) * rows ))
    # echo "s2_combine:${s2_combine}"
    wait
    # echo "python /dicos_ui_home/aronton/tSDRG_random/Subpy/combine.py ""${FILE}"" ${s1_combine}"" ${s2_combine}"
    python /dicos_ui_home/aronton/tSDRG_random/Subpy/combine.py "${FILE}" "${s1_combine}" "${s2_combine}"
    echo  # 輸出一行
    echo "Round${i} finished $(date)"
done
# python /dicos_ui_home/aronton/tSDRG_random/Subpy/combine.py ${FILE}

echo "Job finished $(date)"
