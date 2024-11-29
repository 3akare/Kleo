import { Minus, Plus } from "lucide-react";
import { Button } from "@/components/ui/button";
import {
    Drawer,
    DrawerClose,
    DrawerContent,
    DrawerDescription,
    DrawerFooter,
    DrawerHeader,
    DrawerTitle,
    DrawerTrigger,
} from "@/components/ui/drawer";
import { useState } from "react";

export default function TransferDrawer({refreshTable}:{refreshTable: (p: (prevState: boolean) => boolean)=> void}) {
    const [amount, setAmount] = useState(2000); // Default cryptocurrency amount

    function onClick(adjustment: number) {
        setAmount(Math.max(10, Math.min(100000, amount + adjustment))); // Limits between 10 and 100000
    }

    const submitData = async (amount: number) => {
        try {
            const response = await fetch("https://kleo-dkxb.onrender.com/add_block", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({"data": amount})
            });
            if (!response.ok)
                throw new Error(`Failed to fetch: ${response.statusText}`);
        } catch (err: any) {
            console.error("Error fetching data:", err);
        }
    };

    return (
        <Drawer>
            <DrawerTrigger asChild>
                <Button variant="outline">Transfer Crypto</Button>
            </DrawerTrigger>
            <DrawerContent>
                <div className="mx-auto w-full max-w-xl flex flex-col gap-8">
                    <DrawerHeader>
                        <DrawerTitle>Transfer Cryptocurrency</DrawerTitle>
                        <DrawerDescription>
                            Adjust the amount of cryptocurrency you'd like to transfer.
                        </DrawerDescription>
                    </DrawerHeader>
                    <div className="p-4 pb-0">
                        <div className="flex items-center justify-center space-x-2">
                            <Button
                                variant="outline"
                                size="icon"
                                className="h-8 w-8 shrink-0 rounded-full"
                                onClick={() => onClick(-100)}
                                disabled={amount <= 10}
                            >
                                <Minus />
                                <span className="sr-only">Decrease</span>
                            </Button>
                            <div className="flex-1 text-center">
                                <div className="text-7xl font-bold tracking-tighter">
                                    {amount}
                                </div>
                                <div className="text-[0.70rem] uppercase text-muted-foreground">
                                    Coins
                                </div>
                            </div>
                            <Button
                                variant="outline"
                                size="icon"
                                className="h-8 w-8 shrink-0 rounded-full"
                                onClick={() => onClick(100)}
                                disabled={amount >= 100000}
                            >
                                <Plus />
                                <span className="sr-only">Increase</span>
                            </Button>
                        </div>
                    </div>
                    <DrawerFooter>
                        <DrawerClose asChild>
                            <Button onClick={()=>{
                                submitData(amount);
                                refreshTable((prevState: boolean)=> !prevState)
                            }}>Confirm Transfer</Button>
                        </DrawerClose>
                        <DrawerClose asChild>
                            <Button variant="outline">Cancel</Button>
                        </DrawerClose>
                    </DrawerFooter>
                </div>
            </DrawerContent>
        </Drawer>
    );
}
