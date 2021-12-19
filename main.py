

def run_sh_command(command):
    import subprocess
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()



def main():
    
    demo_models = [
        "python3 tools/demo.py configs/elephant/cityperson/cascade_hrnet.py ./models_pretrained/epoch_5.pth.stu demo/ result_demo/cascade_hrnet-cityperson/",
        "python3 tools/demo.py configs/elephant/cityperson/cascade_mobilenet.py ./models_pretrained/epoch_16.pth.stu demo/ result_demo/cascade_mobilenet/" ,
        "python3 tools/demo.py configs/elephant/cityperson/mgan_vgg.py ./models_pretrained/epoch_1.pth demo/ result_demo/mgan_vgg/" ,
        "python3 tools/demo.py configs/elephant/cityperson/csp_r50.py ./models_pretrained/epoch_72.pth.stu demo/ result_demo/csp_r50/" ,
        "python3 tools/demo.py configs/elephant/caltech/cascade_hrnet.py ./models_pretrained/epoch_14.pth.stu demo/ result_demo/cascade_hrnet-caltech/", 
        "python3 tools/demo.py configs/elephant/eurocity/cascade_hrnet.py ./models_pretrained/epoch_147.pth.stu demo/ result_demo/cascade_hrnet-eurocity/", 
        "python3 tools/demo.py configs/elephant/crowdhuman/cascade_hrnet.py ./models_pretrained/epoch_19.pth.stu demo/ result_demo/cascade_hrnet-crowdhuman/" 
    ]

    for demo_model in demo_models:
        run_sh_command(demo_model)

    print('done')
    
'''

for f in *.jpeg; do mv -- "$f" "${f%.txt}.png" done

'''    

if __name__ == '__main__':
    main()