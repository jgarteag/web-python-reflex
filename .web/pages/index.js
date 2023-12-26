
/** @jsxImportSource @emotion/react */import { Fragment } from "react"
import { Fragment_fd0e7cb8f9fb4669a6805377d925fba0 } from "/utils/stateful_components"
import { Box, HStack, Image as ChakraImage, Spacer, Text, VStack } from "@chakra-ui/react"
import "focus-visible/dist/focus-visible"
import NextHead from "next/head"



export default function Component() {

  return (
    <Fragment>
  <Fragment_fd0e7cb8f9fb4669a6805377d925fba0/>
  <Box>
  <VStack sx={{"bg": "#212529", "position": "sticky", "borderBottom": "0.25em solid #D3D3D3", "paddingX": "2em", "paddingY": "1em", "zIndex": "999", "top": "0", "width": "100%"}}>
  <HStack sx={{"width": "100%"}}>
  <ChakraImage alt={`Juanmas Logo`} src={`logojuan.png`} sx={{"width": "4em", "height": "4em"}}/>
  <Text>
  {`Juanma´s Page`}
</Text>
  <Spacer/>
</HStack>
</VStack>
</Box>
  <NextHead>
  <title>
  {`Juanma´s Reflex App`}
</title>
  <meta content={`Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.`} name={`description`}/>
  <meta content={`favicon.ico`} property={`og:image`}/>
</NextHead>
</Fragment>
  )
}
