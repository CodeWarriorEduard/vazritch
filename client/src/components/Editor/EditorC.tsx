import {IconButton } from '@mui/material';
import Editor, {loader} from '@monaco-editor/react';
import './Editor.styles.css'
import { Box, Tab } from '@mui/material';
import { useState } from 'react';
import { PlayCircle } from '@mui/icons-material';
import {processCode } from '../../services/ApiCalls.service';


function EditorC() {
  const [text, setText] = useState('');
  const [output, setOutput] = useState('');

  loader.init().then((monaco) =>{
    monaco.editor.defineTheme("qleon", {
      base: "vs",
      inherit: true,
      rules: [],
      colors: {
        "editor.foreground": "#CCCCCC", // Color del texto
        "editor.background": "#FFFFFF", // Color de fondo del editor
        "editorCursor.foreground": "#F3EFE0", // Color del cursor
        "editor.lineHighlightBackground": "#333333", // Color de fondo para la línea resaltada
        "editorLineNumber.foreground": "#FFFFFF", // Color de los números de línea
        "editor.selectionBackground": "#666666", // Color de fondo para la selección activa
        "editor.inactiveSelectionBackground": "#666666", // Color de fondo para la selección inactiva
      },
    });
    monaco.editor.setTheme("vazritch");
  })

  const run = async()=>{
    const response = await processCode('/code', null,{ params: {code: text}})
    setOutput(() => {
      return response.map((el: string[], index: number) => {
        return (
          <div key={index}>
            <p className="tabLin" key={index}>{`Content of Line ${index + 1}:`}</p>
            {
              el.length > 0 ? el.map((token: string, idx:number) => (<p className="tabTok" key={idx}> {token}</p>)) :
              <p className="tabTok">Line Empty </p>
            }
            <br />
          </div>
        )
      })
    })
  }

  const handleEditorChange = (value:string|undefined) =>{
    const Ntext = value?? ""; //Quito los saltos de linea.
    setText(Ntext);
  }



  return (
    <div className='main-content'>
      <div className='et-container'>
            <div className='editor-container grid-el'>
            <Box>
              <Tab label="Your Code" style={{backgroundColor:"#222222", borderTopLeftRadius: "10px", color:"white"}}/>
            </Box>
            <Editor height="60vh" width="100%"theme='qleon' onChange={handleEditorChange} className='editor-impl'/>
            </div>
            <div className='terminal-container grid-el'>
              <Box>
                <Tab label="Output" style={{backgroundColor:"#222222", borderTopLeftRadius: "10px", color:"white"}}/>
              </Box>
              {       
                output.length >0?( // Terminar 
                <div className="terminal-impl">{"LEXEMA:"}
                <br />
                <br />
                {output}
                </div> 
                
                ):(
                <div className="terminal-impl">Please write something before running!</div>     
                )                 
              }     
      </div>
      <div className='btn-run'>
        <IconButton onClick={run}>
          <PlayCircle sx={{fontSize:'4rem'}}/>
        </IconButton>
        <p>Run Code</p>
      </div>
    </div>

    </div>
  )
}

export default EditorC