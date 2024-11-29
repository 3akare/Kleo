import TransferDrawer from "@/components/TransferDrawer.tsx";
import TransferTable from "@/components/TransferTable.tsx";
import {useState} from "react";

function App() {
    const [refresh, refreshTable] = useState(true);
    return (
        <>
            <header className={"container mx-auto max-w-7xl"}>
                <nav className={"flex flex-row w-full justify-between items-center px-4 h-16"}>
                    <p className={"text-lg font-semibold"}>Kleo</p>
                    <TransferDrawer refreshTable={refreshTable}/>
                </nav>
            </header>
            <main className={"container mx-auto max-w-7xl px-4 mt-10 h-[calc(100vh-128px)] overflow-y-scroll"}>
                <TransferTable refresh={refresh}/>
            </main>
        </>
    )
}

export default App
